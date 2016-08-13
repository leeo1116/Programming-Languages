module Ascript
  module Control
    module SerdesCharLab
      module SerdesControl_sd16C_txhs_rxd6_ns_02

	  
        def delay_cal(mode,dwell) # mode=0 (phase interpolator), mode=1 (IQ vernier)
          aapl.debug=1
          start = com.sun.jna.ptr.IntByReference.new
          stop = com.sun.jna.ptr.IntByReference.new
          cal_result = aapl.avago_serdes_delay_cal address, mode, dwell, start, stop
          aapl.debug=0
          return start.value,stop.value,cal_result
        end

        def set_pi(offset)
          #offset = offset % 127
          esb_dma.PI_UPDATE.set 0
          esb_dma.sync
          if ((offset >= 0) && (offset <= 31))
            select = 3
            bt1 = 0xffff;
            bt2 = 0xffff;
            while (offset > 0)
              if (bt1 == 0) then
                bt2 = bt2 / 2;
              else
                bt1 = bt1 / 2;
              end
              offset = offset - 1
            end
          elsif ((offset >= 32) && (offset <= 63))
            select = 6
            bt1 = 0xffff;
            bt2 = 0xffff;
            while (offset < 63)
              if (bt1 == 0) then
                bt2 = bt2 / 2;
              else
                bt1 = bt1 / 2;
              end
              offset = offset + 1
             end
          elsif ((offset >= 64) && (offset <= 95))
            select = 12
            bt1 = 0xffff;
            bt2 = 0xffff;
            while (offset > 64)
              if (bt1 == 0) then
                bt2 = bt2 / 2;
              else
                bt1 = bt1 / 2;
              end
              offset = offset - 1
            end
          elsif ((offset >= 96) && (offset <= 127))
            select = 9
            bt1 = 0xffff;
            bt2 = 0xffff;
            while (offset < 127)
              if (bt1 == 0) then
                bt2 = bt2 / 2;
              else
                bt1 = bt1 / 2;
              end
              offset = offset + 1
            end
          end
          nbt1 = 0xffff - bt1
          nbt2 = 0xffff - bt2
          esb_dma.PI_BT_15_0.set bt1
          esb_dma.PI_BT_31_16.set bt2
          esb_dma.PI_NT_15_0.set nbt1
          esb_dma.PI_NT_31_16.set nbt2
          esb_dma.sync
          esb_dma.PI_UPDATE.set 1
          esb_dma.PI_SEL.set select
          esb_dma.sync
        end

        def pi_cal_16nm
          start = 0 
          stop = 127 
          best_point = 95 

          min_errors = 1000000000
               
          #DDR 147/0x93 async DFE_MISC_CTL2
          #REG  15:12      8   RW TAP_SEL
          #REG   11:8      8   RW T2CLK1_SEL
          #REG    7:4      8   RW T2CLK0_SEL
          #REG    3:0      8   RW D2CLK0_SEL
          mem_wr :type => :esb, :addr => 0x93, :data => 0x8828
                    
          #ADDR 183/0xb7 async DFE_CK_OBS
          #REG  15:12      1   RW TAP_DEL_SEL
          #REG   11:8      1   RW T2CLK1_DEL_SEL
          #REG    7:4      1   RW T2CLK0_DEL_SEL
          #REG    3:0      1   RW D2CLK0_DEL_SEL
          mem_wr :type => :esb, :addr => 0xb7, :data => 0x2282
                    
          (start..stop).each { |offset|
            set_pi(offset)
            get_errors :type => :lsb, :reset => true
            sleep 0.01  
            errors = get_errors :type => :lsb, :reset => true
            if (errors == 0) && (start == 0)
              start = offset
            elsif errors == 0
              stop = offset
            end
            if (start == 0) && (errors < min_errors)
              min_errors = errors
              best_point = offset
            end
            puts "#### #{offset} #{start} #{stop} #{(stop-start)/2+start} #{offset} #{errors}"
          }        

          if start != 0 
            x_out = (stop - start)/2 + start
          else
            x_out = best_point
          end
          puts "#### horizontal center: #{x_out}"

          127.downto(x_out) {|phase|
            #puts "Decrementing PI back to horizontal center of eye: #{phase}"
            set_pi(phase)
          }

          sleep 0.1
          get_errors :type => :lsb, :reset => true
          printf("#### pi_start:%d,pi_stop:%d,pi_cal:%d,errors:%d \n",start,stop,x_out,get_errors)
          return start,stop,x_out
        end
		
        def delay_cal_16nm
          start = 0
          stop = 41
          #best_point = 0
          best_point = 32 
          min_errors = 1000000000
          array = [0xd6, 0xce, 0xd0, 0xb5, 0x95, 0x90, 0xa5, 0xa1, 0x88, 0x84, 0x56, 0x4e, 0x46, 0x50, 0x45, 0x44, 0x06, 0x10, 0x22, 0x03,  0x01, 0x03, 0x22, 0x10, 0x06, 0x44, 0x45, 0x50, 0x46, 0x4e, 0x56, 0x84, 0x88, 0xa1, 0xa5, 0x90, 0x95, 0xb5, 0xd0, 0xce, 0xd6]
        
          #DDR 147/0x93 async DFE_MISC_CTL2
          #REG  15:12      8   RW TAP_SEL
          #REG   11:8      8   RW T2CLK1_SEL
          #REG    7:4      8   RW T2CLK0_SEL
          #REG    3:0      8   RW D2CLK0_SEL
          mem_wr :type => :esb, :addr => 0x93, :data => 0x2222
            
          #ADDR 183/0xb7 async DFE_CK_OBS
          #REG  15:12      1   RW TAP_DEL_SEL
          #REG   11:8      1   RW T2CLK1_DEL_SEL
          #REG    7:4      1   RW T2CLK0_DEL_SEL
          #REG    3:0      1   RW D2CLK0_DEL_SEL
          mem_wr :type => :esb, :addr => 0xb7, :data => 0x2242
            
          #ADDR 179/0xb3 async DFE_D2CLK0_DEL
          #REG   15:8      0   RW TAP_CTL
          #REG    7:0      0   RW D2CLK0_CTL
          #
          #############################################
          ##   dfe_t2clk_del
          ##   Register_type = Base_Register
          #############################################
          #ADDR 180/0xb4 async DFE_T2CLK_DEL
          #REG   15:8      0   RW T2CLK1_CTL // test
          #REG    7:0      0   RW T2CLK0_CTL // edge
          #
          puts "#### #{array.size}"
          x_out = 0
          array.each_index do |x|
            if x <= 19
              mem_rmw :type => :esb, :addr => 0xb3, :data => array[x], :mask => 0xff # main
              mem_rmw :type => :esb, :addr => 0xb4, :data => 0, :mask => 0xff # edge
            else
              mem_rmw :type => :esb, :addr => 0xb3, :data => 0, :mask => 0xff # main
              mem_rmw :type => :esb, :addr => 0xb4, :data => array[x], :mask => 0xff # edge
            end
            get_errors :type => :lsb, :reset => true
            #sleep 0.300 # Aaron requested to reduce from 300mS to 10mS
            sleep 0.010
            errors = get_errors :type => :lsb, :reset => true
        
            if (errors == 0) && (start == 0)
              start = x
            elsif errors == 0
              stop = x
            end
        
            if (start == 0) && (errors < min_errors)
              min_errors = errors
              best_point = x
            end
            
            puts "## #{x} #{start} #{stop} #{(stop-start)/2+start} #{array[x]} #{errors}"
        
            x_out = x # pass x out of the loop
          end ## each_index
        
          if start != 0
            x_out = (stop - start)/2 + start
          else
            x_out = best_point
          end
        
          puts "#### Setting delay to: #{x_out}"
        
          if x_out <= 19
            mem_rmw :type => :esb, :addr => 0xb3, :data => array[x_out], :mask => 0xff # main
            mem_rmw :type => :esb, :addr => 0xb4, :data => 0, :mask => 0xff # edge
          else
            mem_rmw :type => :esb, :addr => 0xb3, :data => 0, :mask => 0xff # main
            mem_rmw :type => :esb, :addr => 0xb4, :data => array[x_out], :mask => 0xff # edge
          end
        
          sleep 0.1
          get_errors :type => :lsb, :reset => true
        
          x_out
        end

        
        def set_lb_gain(lb_gain=0)
          esb_dma.PDLB.set lb_gain # 2bits default 3
          esb_dma.sync
        end

        def set_d6_tx_eq(pre=0,post=0,atten=0)
          set_tx_eq :pre => pre
          set_tx_eq :post => post 
          set_tx_eq :atten => atten 
        end

        def set_d6_dfe_off
          aapl.avago_spico_int address, 0x26, 0x3000 # Gain
          aapl.avago_spico_int address, 0x26, 0x3100 # tap2
          aapl.avago_spico_int address, 0x26, 0x3200 # tap3
          aapl.avago_spico_int address, 0x26, 0x3300 # tap4
          aapl.avago_spico_int address, 0x26, 0x3400 # tap5
          aapl.avago_spico_int address, 0x26, 0x3500 # tap6
          aapl.avago_spico_int address, 0x26, 0x3600 # tap7
          aapl.avago_spico_int address, 0x26, 0x3700 # tap8
          aapl.avago_spico_int address, 0x26, 0x3800 # tap9
          aapl.avago_spico_int address, 0x26, 0x3900 # tap10
          aapl.avago_spico_int address, 0x26, 0x3A00 # tap11
          aapl.avago_spico_int address, 0x26, 0x3B00 # tap12
        end

        def set_d6_dfe_railEven(dfeGain=0x3000)
          aapl.avago_spico_int address, 0x26, dfeGain # Gain
          aapl.avago_spico_int address, 0x26, 0x310F  # tap2
          aapl.avago_spico_int address, 0x26, 0xB20F  # tap3
          aapl.avago_spico_int address, 0x26, 0x330F  # tap4
          aapl.avago_spico_int address, 0x26, 0xB40F  # tap5
          aapl.avago_spico_int address, 0x26, 0x350F  # tap6
          aapl.avago_spico_int address, 0x26, 0xB60F  # tap7
          aapl.avago_spico_int address, 0x26, 0x370F  # tap8
          aapl.avago_spico_int address, 0x26, 0xB80F  # tap9
          aapl.avago_spico_int address, 0x26, 0x390F  # tap10
          aapl.avago_spico_int address, 0x26, 0xBA0F  # tap11
          aapl.avago_spico_int address, 0x26, 0x3B0F  # tap12
        end

        def set_d6_dfe_railOdd(dfeGain=0x3000)
          aapl.avago_spico_int address, 0x26, dfeGain # Gain
          aapl.avago_spico_int address, 0x26, 0xB10F  # tap2
          aapl.avago_spico_int address, 0x26, 0x320F  # tap3
          aapl.avago_spico_int address, 0x26, 0xB30F  # tap4
          aapl.avago_spico_int address, 0x26, 0x340F  # tap5
          aapl.avago_spico_int address, 0x26, 0xB50F  # tap6
          aapl.avago_spico_int address, 0x26, 0x360F  # tap7
          aapl.avago_spico_int address, 0x26, 0xB70F  # tap8
          aapl.avago_spico_int address, 0x26, 0x380F  # tap9
          aapl.avago_spico_int address, 0x26, 0xB90F  # tap10
          aapl.avago_spico_int address, 0x26, 0x3A0F  # tap11
          aapl.avago_spico_int address, 0x26, 0xBB0F  # tap12
        end

        def get_error_count (show=0)
          errcount1 = (lsb_dma.ERROR_HI.get << 16)   + lsb_dma.ERROR_LO.get
          errcount2 = (lsb_dma.ERROR_HI_2.get << 16) + lsb_dma.ERROR_LO_2.get
          puts "Error1= #{"%09d" % errcount1}   Error2= #{"%09d" % errcount2}" unless (show==0)
          return errcount1,errcount2;
        end

        def get_tx_cf
            tx_therm_weight = 8
            tx_cf_bin = esb_dma.TX_CAL_DAC_BIN.get
            tx_cf_therm = esb_dma.TX_CAL_DAC_THERM.get
            @tx_cf = (("%08b"%tx_cf_therm).chars.map{ |x| x.to_i*tx_therm_weight} << tx_cf_bin ).inject{ |sum,x| sum+x }
            printf("tx_cf:%3d\n",@tx_cf)
            return @tx_cf
        end

        def get_tx_pll_gains
          @tx_bb_gain = esb_dma.TX_BB_GAIN.get
          @tx_int_gain = esb_dma.TX_INT_GAIN.get
          printf("Tx PLL Gains: BB=%d, INT=%d\n",@tx_bb_gain,@tx_int_gain)
          return @tx_bb_gain,@tx_int_gain
        end

        def get_rx_cf
          rx_therm_weight = 8
          rx_cf_bin = esb_dma.RX_CAL_DAC_BIN.get
          rx_cf_therm = esb_dma.RX_CAL_DAC_THERM.get
          @rx_cf = (("%08b"%rx_cf_therm).chars.map{ |x| x.to_i*rx_therm_weight} << rx_cf_bin ).inject{ |sum,x| sum+x }
          printf("rx_cf:%3d\n",@rx_cf)
          return @rx_cf
        end

        def get_rx_pll_gains
          @rx_bb_gain = esb_dma.RX_NML_BB_GAIN.get
          @rx_int_gain = esb_dma.RX_NML_INT_GAIN.get
          printf("Rx PLL Gains: BB=%d, INT=%d \n",@rx_bb_gain,@rx_int_gain)
          return @rx_bb_gain,@rx_int_gain
        end

        def get_rx_flock
          @rx_flock = lsb_dma.RX_FINE_FLOCK.get
          printf("rx_flock: %d\n",@rx_flock)
          return @rx_flock
        end

        def get_pll_status
          @tx_cf = get_tx_cf  
          @tx_bb_gain = esb_dma.TX_BB_GAIN.get
          @tx_int_gain = esb_dma.TX_INT_GAIN.get
          @rx_flock = lsb_dma.RX_FINE_FLOCK.get
          @rx_cf = get_rx_cf
          @rx_bb_gain = esb_dma.RX_NML_BB_GAIN.get
          @rx_int_gain = esb_dma.RX_NML_INT_GAIN.get
          printf("Rx: flock:%3d  CF:%2d  BB Gain:%2d  INT Gain:%2d \n",@rx_flock,@rx_cf,@rx_bb_gain,@rx_int_gain)
          printf("Tx:            CF:%2d  BB Gain:%2d  INT Gain:%2d \n",@tx_cf,@tx_bb_gain,@tx_int_gain)
        end
          
        def get_rx_state
            state    = get_dfe_state
            @vos0    = state.vos[0]
            @vos1    = state.vos[1]
            @vos2    = state.vos[2]
            @vos3    = state.vos[3]
            @vos4    = state.vos[4]
            @vos5    = state.vos[5]
            @vos6    = state.vos[6]
            @vos7    = state.vos[7]
            @dc      = state.dc
            @lf      = state.lf
            @hf      = state.hf
			#fixme I had to comment these out because GAINHF is not defined
            #@hf_dgen = dec2therm(decVal=(esb_dma.GAINHF.get >> 8).to_i)
            #@hf_dq   = dec2therm(decVal=(esb_dma.GAINHF.get & 0x00ff).to_i)
            @bw      = state.bw
            @gain    = state.dfeGAIN
            @tap1    = state.dfeTAP1.round
            @tap2    = state.dfeTAP[0]
            @tap3    = state.dfeTAP[1]
            @tap4    = state.dfeTAP[2]
            @tap5    = state.dfeTAP[3]
            @tap6    = state.dfeTAP[4]
            @tap7    = state.dfeTAP[5]
            @tap8    = state.dfeTAP[6]
            @tap9    = state.dfeTAP[7]
            @tap10   = state.dfeTAP[8]
            @tap11   = state.dfeTAP[9]
            @tap12   = state.dfeTAP[10]
            @tap13   = state.dfeTAP[11]

            printf("VOS: vos0:%3d  vos1:%3d  vos2:%3d  vos3:%3d  vos4:%3d  vos5:%3d  vos6:%3d  vos7:%3d\n",@vos0,@vos1,@vos2,@vos3,@vos4,@vos5,@vos6,@vos7)
            #printf("CTLE: DC:%3d  LF:%2d  HF:%2d  HF_DGEN:%1d  HF_DQ:%1d  BW:%2d \n",@dc,@lf,@hf,@hf_dgen,@hf_dq,@bw)
			printf("CTLE: DC:%3d  LF:%2d  HF:%2d  BW:%2d \n",@dc,@lf,@hf,@bw)
            printf("DFE: dfeGAIN:%2d  tap1:%2d  tap2:%2d  tap3:%2d  tap4:%2d  tap5:%2d  tap6:%2d  tap7:%2d  tap8:%2d  tap9:%2d  tap10:%2d  tap11:%2d  tap12:%2d tap13:%2d\n",@gain,@tap1,@tap2,@tap3,@tap4,@tap5,@tap6,@tap7,@tap8,@tap9,@tap10,@tap11,@tap12,@tap13)
            #return @vos0, @vos1, @vos2, @vos3, @vos4, @vos5, @vos6, @vos7, @dc, @lf, @hf, @hf_dgen, @hf_dq, @bw, @gain, @tap1, @tap2, @tap3, @tap4, @tap5, @tap6, @tap7, @tap8, @tap9, @tap10, @tap11, @tap12, @tap13
			return @vos0, @vos1, @vos2, @vos3, @vos4, @vos5, @vos6, @vos7, @dc, @lf, @hf, @bw, @gain, @tap1, @tap2, @tap3, @tap4, @tap5, @tap6, @tap7, @tap8, @tap9, @tap10, @tap11, @tap12, @tap13
 
		end

        def rx_tune_wait(timeout=20)
          sleepCount = 0
          rxTuneStatus =  aapl.avago_spico_int address, 0x126, 0x0b00
          while ((rxTuneStatus != 128) and (sleepCount < timeout))
            sleep(1)
            rxTuneStatus =  aapl.avago_spico_int address, 0x126, 0x0b00
            sleepCount += 1
          end
          printf("Rx tuning completed in %d seconds \n",sleepCount)
        end

        def set_rx_pll_gains(rx_bb_gain=4,rx_int_gain=14)
          esb_dma.RX_NML_BB_GAIN.set rx_bb_gain
          esb_dma.RX_NML_INT_GAIN.set rx_int_gain
          esb_dma.sync
          printf("Rx PLL gains set to: BB=%d, INT=%d \n",esb_dma.RX_NML_BB_GAIN.get,esb_dma.RX_NML_INT_GAIN.get)
        end

        def get_sample_errors(samples="1M")
          case samples
            when "max"
              aapl.avago_spico_int address, 0x017, 0x0000 # reset error counter
              aapl.avago_spico_int address, 0x203, 0xFFFF # do 344B samples
              aapl.avago_spico_int address, 0x103, 0xFFFF #
            when "1M"
              aapl.avago_spico_int address, 0x017, 0x0000 # reset error counter
              aapl.avago_spico_int address, 0x203, 0x000F # do 1M samples
              aapl.avago_spico_int address, 0x103, 0x4240 #
            else
              puts "invalid sample value"
          end #case
          aapl.avago_spico_int address, 0x003, 0x0203 # mission ^ patgen
          error_count_wait
          #errors = (lsb_dma.ERROR_HI.get << 16) + lsb_dma.ERROR_LO.get
          errors=get_errors :type => :lsb, :reset => true
		  return errors;
       
		end
  
        def error_count_wait
          stat=aapl.avago_spico_int address, 0x1f, 0x0
          timeout = 100
          while (((stat & 0x10) != 0) and (timeout > 0))
            stat = aapl.avago_spico_int address, 0x1f, 0x0
            timeout = timeout - 1
          end
          #printf("error count timecount: %3d\n",timeout)
        end

        def get_and_check_errors(samples="1M", pattern)
          @errors = get_sample_errors(samples)
          if (@errors == 0)
            pat = get_rx_cmp_data
            set_rx_cmp_data(input=pattern) 
            @pattern_errors = get_sample_errors(samples)
            if (@pattern_errors == 0)
              @errors = -22
            else
              @errors = 0
            end
            set_rx_cmp_data(input=pattern)
          end
          #puts @errors
          if (samples == "1M")
            @bit_error_ratio = @errors.to_f/(40*1.0e+06)
          else
            @bit_error_ratio = @errors.to_f/(40*4294967295)
          end
          printf("Errors: %d, BER: %.3E\n",@errors,@bit_error_ratio)
          return @errors, @bit_error_ratio
        end

        def inject_tx_err(n_errors)
          aapl.avago_spico_int address, 0x1b, n_errors
        end 

        def error_reset
			aapl.avago_spico_int address,0x017,0x000 #reset error counter
            printf("Error counter reset\n")
          end

          def error_count_inf_dwell
            aapl.avago_spico_int address, 0x203, 0x0 # set for infinite dwell
            aapl.avago_spico_int address, 0x103, 0x0 #
            aapl.avago_spico_int address, 0x003, 0x0203 # mission ^ patgen
            printf("Error counter set for infinite dwell\n")
          end

          def error_count
            @errors = (lsb_dma.ERROR_HI.get << 16) + lsb_dma.ERROR_LO.get
            printf("Errors:%d\n",@errors)
            return @errors
          end

          def error_count_halt
            lsb_dma.ERROR_COUNT_FORCE_ACTIVE.set 0b0
            lsb_dma.sync
            printf("Error count halted\n")
          end

          def error_count_resume
            lsb_dma.ERROR_COUNT_FORCE_ACTIVE.set 0b1
            lsb_dma.sync
            printf("Error count resuming\n")
          end

        def rx_pll_f2i_clk_obs
          esb_dma.SEL_BSBCK.set 1
          esb_dma.TX_OBS_EN.set 1
          esb_dma.PIDIV_EN.set 1
          esb_dma.SEL_RX_OBS.set 1
          esb_dma.SEL_DFE_OBS.set 1
          esb_dma.SEL_DECEL_OBS.set 0
          esb_dma.SEL_PI_OBS.set 1
          esb_dma.TEST_CKMUX_EN.set 1
          esb_dma.sync
        end

        def rx_pll_f2q_clk_obs
          esb_dma.SEL_BSBCK.set 1
          esb_dma.TX_OBS_EN.set 1
          esb_dma.PIDIV_EN.set 1
          esb_dma.SEL_RX_OBS.set 1
          esb_dma.SEL_DFE_OBS.set 1
          esb_dma.SEL_DECEL_OBS.set 0
          esb_dma.SEL_PI_OBS.set 1
          esb_dma.TEST_CKMUX_EN.set 2
          esb_dma.sync
        end

        def rx_pll_f2r_clk_obs
          esb_dma.SEL_BSBCK.set 1
          esb_dma.TX_OBS_EN.set 1
          esb_dma.PIDIV_EN.set 1
          esb_dma.SEL_RX_OBS.set 1
          esb_dma.SEL_DFE_OBS.set 1
          esb_dma.SEL_DECEL_OBS.set 0
          erdes.rbSb_dma.SEL_BSBCK.set 1
          esb_dma.TX_OBS_EN.set 1
          esb_dma.SEL_RX_OBS.set 1
          esb_dma.SEL_DFE_OBS.set 1
          esb_dma.SEL_DECEL_OBS.set 0
          esb_dma.SEL_PI_OBS.set 0
          esb_dma.RX_TEST_CLK_CNTL_0.set 1
          esb_dma.RX_TEST_CLK_CNTL_1.set 0
          esb_dma.sync
        end

        def rx_refclk_obs
          esb_dma.SEL_BSBCK.set 1
          esb_dma.TX_OBS_EN.set 1
          esb_dma.SEL_RX_OBS.set 1
          esb_dma.SEL_DFE_OBS.set 1
          esb_dma.SEL_DECEL_OBS.set 0
          esb_dma.SEL_PI_OBS.set 0
          esb_dma.RX_TEST_CLK_CNTL_0.set 0
          esb_dma.RX_TEST_CLK_CNTL_1.set 1
          esb_dma.sync
        end

        def tx_divx_clk_obs
          esb_dma.SEL_BSBCK.set 1
          esb_dma.TX_OBS_EN.set 1
          esb_dma.SEL_RX_OBS.set 0
          esb_dma.SEL_TXPHB_OBS.set 0
          esb_dma.TX_TEST_CLK_CNTL_0.set 1
          esb_dma.TX_TEST_CLK_CNTL_1.set 0
          esb_dma.sync
        end

        def tx_refclk_obs
          esb_dma.SEL_BSBCK.set 1
          esb_dma.TX_OBS_EN.set 1
          esb_dma.SEL_RX_OBS.set 0
          esb_dma.SEL_TXPHB_OBS.set 0
          esb_dma.TX_TEST_CLK_CNTL_0.set 0
          esb_dma.TX_TEST_CLK_CNTL_1.set 1
          esb_dma.sync
        end

        def rx_dfe_d0_obs
          esb_dma.SEL_BSBCK.set 1
          esb_dma.TX_OBS_EN.set 1
          esb_dma.PIDIV_EN.set 1
          esb_dma.SEL_RX_OBS.set 1
          esb_dma.SEL_DFE_OBS.set 0
          esb_dma.SEL_DECEL_OBS.set 0
          esb_dma.CK8OBS_SEL.set 0x18
          esb_dma.sync
        end

        def rx_decel_f2_clk_obs
          esb_dma.SEL_BSBCK.set 1
          esb_dma.TX_OBS_EN.set 1
          esb_dma.PIDIV_EN.set 1
          esb_dma.SEL_RX_OBS.set 1
          esb_dma.SEL_DFE_OBS.set 1
          esb_dma.SEL_DECEL_OBS.set 1
          esb_dma.SEL_PI_OBS.set 1
          esb_dma.DECEL_SMPL_EN.set 1
          esb_dma.DECEL_SMPL_CTL.set 3
          esb_dma.sync
        end

        def rx_decel_fw_clk_obs
          esb_dma.SEL_BSBCK.set 1
          esb_dma.TX_OBS_EN.set 1
          esb_dma.PIDIV_EN.set 1
          esb_dma.SEL_RX_OBS.set 1
          esb_dma.SEL_DFE_OBS.set 1
          esb_dma.SEL_DECEL_OBS.set 1
          esb_dma.SEL_PI_OBS.set 1
          esb_dma.DECEL_SMPL_EN.set 1
          esb_dma.DECEL_SMPL_CTL.set 1
          esb_dma.sync
        end

        def rx_decel_data_obs
          esb_dma.SEL_BSBCK.set 1
          esb_dma.TX_OBS_EN.set 1
          esb_dma.PIDIV_EN.set 1
          esb_dma.SEL_RX_OBS.set 1
          esb_dma.SEL_DFE_OBS.set 1
          esb_dma.SEL_DECEL_OBS.set 1
          esb_dma.SEL_PI_OBS.set 1
          esb_dma.DECEL_SMPL_EN.set 1
          esb_dma.DECEL_SMPL_CTL.set 0
          esb_dma.sync
        end

        def rx_decel_f4_clk_obs
          esb_dma.SEL_BSBCK.set 1
          esb_dma.TX_OBS_EN.set 1
          esb_dma.PIDIV_EN.set 1
          esb_dma.SEL_RX_OBS.set 1
          esb_dma.SEL_DFE_OBS.set 1
          esb_dma.SEL_DECEL_OBS.set 1
          esb_dma.SEL_PI_OBS.set 1
          esb_dma.DECEL_SMPL_EN.set 0
          esb_dma.DECEL_SMPL_CTL.set 4
          esb_dma.sync
        end

        def rx_dfe_f2i_obs
          esb_dma.SEL_BSBCK.set 1
          esb_dma.TX_OBS_EN.set 1
          esb_dma.PIDIV_EN.set 1
          esb_dma.SEL_RX_OBS.set 1
          esb_dma.SEL_DFE_OBS.set 0
          esb_dma.SEL_DECEL_OBS.set 0
          esb_dma.CK8OBS_SEL.set 0x14
          esb_dma.sync
        end

        def rx_dfe_f2q_obs
          esb_dma.SEL_BSBCK.set 1
          esb_dma.TX_OBS_EN.set 1
          esb_dma.PIDIV_EN.set 1
          esb_dma.SEL_RX_OBS.set 1
          esb_dma.SEL_DFE_OBS.set 0
          esb_dma.SEL_DECEL_OBS.set 0
          esb_dma.CK8OBS_SEL.set 0x12
          esb_dma.sync
        end

        def rx_dfe_f2r_obs
          esb_dma.SEL_BSBCK.set 1
          esb_dma.TX_OBS_EN.set 1
          esb_dma.PIDIV_EN.set 1
          esb_dma.SEL_RX_OBS.set 1
          esb_dma.SEL_DFE_OBS.set 0
          esb_dma.SEL_DECEL_OBS.set 0
          esb_dma.CK8OBS_SEL.set 0x11
          esb_dma.sync
        end

        def rx_dfe_cdc_phd_obs
          esb_dma.SEL_BSBCK.set 1
          esb_dma.TX_OBS_EN.set 1
          esb_dma.PIDIV_EN.set 1
          esb_dma.SEL_RX_OBS.set 1
          esb_dma.SEL_DFE_OBS.set 0
          esb_dma.SEL_DECEL_OBS.set 0
          esb_dma.CK8OBS_SEL.set 0x40
          esb_dma.sync
        end

        def rx_dfe_cdc_dec_obs
          esb_dma.SEL_BSBCK.set 1
          esb_dma.TX_OBS_EN.set 1
          esb_dma.PIDIV_EN.set 1
          esb_dma.SEL_RX_OBS.set 1
          esb_dma.SEL_DFE_OBS.set 0
          esb_dma.SEL_DECEL_OBS.set 0
          esb_dma.CK8OBS_SEL.set 0x20
          esb_dma.sync
        end

        def rx_dfe_phd_obs
          esb_dma.SEL_BSBCK.set 1
          esb_dma.TX_OBS_EN.set 1
          esb_dma.PIDIV_EN.set 1
          esb_dma.SEL_RX_OBS.set 1
          esb_dma.SEL_DFE_OBS.set 0
          esb_dma.SEL_DECEL_OBS.set 0
          esb_dma.CK8OBS_SEL.set 0x80
          esb_dma.sync
        end

        def hex2gray(hexVal=0)
          for hexVal in (0..15).step(1) do
            grayVal = (hexVal>>1)^hexVal
            #printf "hexVal=0x%x grayVal=0x%x\n",hexVal,grayVal
          end
          return grayVal
        end

        def dec2therm(decVal=0)
          thermVal = (Math.log(decVal+1)/Math.log(2)).to_i
          return thermVal
        end
        
		#########################
		##### RX/TX PRBS ########
		#########################
		def set_tx_rx_pat(patt)
			lpatt=patt.downcase
			case lpatt
				when 'prbs7'
					#puts "pattern : PRBS7"
					set_tx_data_sel(input=:prbs7)
					set_rx_cmp_data(input=:prbs7)
				when 'prbs9'
					#puts "pattern : PRBS9"
					set_tx_data_sel(input=:prbs9)
					set_rx_cmp_data(input=:prbs9)
				when 'prbs11' 
					#puts "pattern : PRBS11"
					set_tx_data_sel(input=:prbs11)
					set_rx_cmp_data(input=:prbs11)
				when 'prbs15'
					#puts "pattern : PRBS15"
					set_tx_data_sel(input=:prbs15)
					set_rx_cmp_data(input=:prbs15)
				when 'prbs23'
					#puts "pattern : PRBS23"
					set_tx_data_sel(input=:prbs23)
					set_rx_cmp_data(input=:prbs23)
				when 'prbs31'
					#puts "pattern : prbs31"
					set_tx_data_sel(input=:prbs31)
					set_rx_cmp_data(input=:prbs31)	
			end # Case
		end # def
		
		def write_eye_btc_file(addr, filename)

		  #fixme this was just copied over from 16nm .. may not work
		  
		  # Get log type enumeration value
		  log_type = AAPL::Aapl_log_type_t.const_get "AVAGO_INFO"

		  # Get AAPL manager
		  aapl = Ascript::Control::System.instances[0].aapl

		  #puts" Create eye structures"
			config = aapl.avago_serdes_eye_config_construct
			data = aapl.avago_serdes_eye_data_construct
			
			#fixme I need to figure out what cmp_mode and data are used for all the calls in the code
			#puts"data_qual"
			# config.ec_data_qual.d6_data_qual=0 #@AVAGO_SERDES_RX_DATA_QUAL_UNQUAL==0 , will use all bits
			#puts"cmp_mode"
			# config.ec_cmp_mode=0x0120 #@AVAGO_SERDES_RX_CMP_MODE_TEST_PATGEN = 0x120, @AVAGO_SERDES_RX_CMP_MODE_TEST_PATGEN=0x200

      puts"Setting max dwell to 1e10 for eye diagram"
			config.ec_max_dwell_bits=0x5F5E100 #dwell 1e10
			# config.ec_y_points=256
			
			#puts config

		  # Get eye (can check return code for < 0)
		  rc = aapl.avago_serdes_eye_get addr, config, data
		  
		  vbtc_out= data.ed_vbtc
		  puts "For the eye saved the vertical bathtub curve eye opening at BER 1e-10 is #{vbtc_out.vert_eye_1e10} mV"
		  
		  # Write eye data to file
		  aapl.avago_serdes_eye_data_write_file filename, data

		  # Destroy eye structures
		  aapl.avago_serdes_eye_data_destruct data
		  aapl.avago_serdes_eye_config_destruct config

		end #def write_eye_btc_file
		
		def get_eye_height(addr)

		  # Get log type enumeration value
		  log_type = AAPL::Aapl_log_type_t.const_get "AVAGO_INFO"

		  # Get AAPL manager
		  aapl = Ascript::Control::System.instances[0].aapl

		  # Create eye structures
			config = aapl.avago_serdes_eye_config_construct
			data = aapl.avago_serdes_eye_data_construct

			config.ec_eye_type = 1 #AVAGO_EYE_HEIGHT
			
			#puts config

		  # Get eye (can check return code for < 0)
		  rc = aapl.avago_serdes_eye_get addr, config, data

		  # Write eye data to file
		  #aapl.avago_serdes_eye_data_write_file filename, data
		  eye_h_mV = data.ed_height_mV
		  puts "The eye height is #{eye_h_mV} mV"
		  

		  # Destroy eye structures
		  aapl.avago_serdes_eye_data_destruct data
		  aapl.avago_serdes_eye_config_destruct config
		  
		  return eye_h_mV #vbtc eye height in mV

		  end #def get_eye_height
		  
		  def get_vbtc(addr)

		  #fixme should add option for changing dwell
		  
		  # Get log type enumeration value
		  log_type = AAPL::Aapl_log_type_t.const_get "AVAGO_INFO"

		  # Get AAPL manager
		  aapl = Ascript::Control::System.instances[0].aapl

		  # Create eye structures
			config = aapl.avago_serdes_eye_config_construct
			data = aapl.avago_serdes_eye_data_construct

			#fixme I need to figure out what cmp_mode and data are used for all the calls in the code
			#puts"data_qual"
			# config.ec_data_qual.d6_data_qual=0 #@AVAGO_SERDES_RX_DATA_QUAL_UNQUAL==0 , will use all bits
			#puts"cmp_mode"

			# config.ec_cmp_mode=0x0120 #@AVAGO_SERDES_RX_CMP_MODE_TEST_PATGEN = 0x120, @AVAGO_SERDES_RX_CMP_MODE_TEST_PATGEN=0x200
			# config.ec_cmp_mode=0x0200

      #puts config
			#puts" setting dwell to 1e9"
			config.ec_max_dwell_bits=0x5F5E100 #dwell 1e10
			#config.ec_y_points=256
			
			#puts"select set to eye height"
			#config.ec_eye_type = 1 #AVAGO_EYE_HEIGHT
			
			#puts config

		  # Get eye (can check return code for < 0)
		  rc = aapl.avago_serdes_eye_get addr, config, data

		  #Write eye data to file
		  #aapl.avago_serdes_eye_data_write_file filename, data
		  vbtc_out= data.ed_vbtc
		  
		  # Destroy eye structures
		  aapl.avago_serdes_eye_data_destruct data
		  aapl.avago_serdes_eye_config_destruct config
		  
		  return vbtc_out #vbtc 
		  
		  end #def get_vbtc
		  
      def get_hvbtc(addr)

      #fixme should add option for changing dwell
      
      # Get log type enumeration value
      log_type = AAPL::Aapl_log_type_t.const_get "AVAGO_INFO"

      # Get AAPL manager
      aapl = Ascript::Control::System.instances[0].aapl

      # Create eye structures
      config = aapl.avago_serdes_eye_config_construct
      data = aapl.avago_serdes_eye_data_construct

      #fixme I need to figure out what cmp_mode and data are used for all the calls in the code
      #puts"data_qual"
      # config.ec_data_qual.d6_data_qual=0 #@AVAGO_SERDES_RX_DATA_QUAL_UNQUAL==0 , will use all bits
      #puts"cmp_mode"

      # config.ec_cmp_mode=0x0120 #@AVAGO_SERDES_RX_CMP_MODE_TEST_PATGEN = 0x120, @AVAGO_SERDES_RX_CMP_MODE_TEST_PATGEN=0x200
      # config.ec_cmp_mode=0x0200

      #puts config
      #puts" setting dwell to 1e9"
      config.ec_max_dwell_bits=0x5F5E100 #dwell 1e10
      #config.ec_y_points=256
      
      #puts"select set to eye height"
      #config.ec_eye_type = 1 #AVAGO_EYE_HEIGHT
      
      #puts config

      # Get eye (can check return code for < 0)
      rc = aapl.avago_serdes_eye_get addr, config, data

      #Write eye data to file
      #aapl.avago_serdes_eye_data_write_file filename, data
      hbtc_out = data.ed_hbtc
      vbtc_out = data.ed_vbtc
      # Destroy eye structures
      aapl.avago_serdes_eye_data_destruct data
      aapl.avago_serdes_eye_config_destruct config
      
      return hbtc_out, vbtc_out #hbtc, vbtc_out
      
      end #def get_hbtc
      
		end
		
      end
    end
  end
