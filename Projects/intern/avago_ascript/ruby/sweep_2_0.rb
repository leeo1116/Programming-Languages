##sweep_simba_ACS.rb
##Authors: Cattalen Annullnulli-Pelard (CAP)based on code from Anthony Sweeney (ACS)
## 
## Version 1.0 6/22/2015  ACS
## sweep tx and rx parameters for a single channel on the hawks board
## Version 1.1 7/16/2015  ACS
## - Driven by Confi_sweep.csv in ../sweep  directory
## - Sweep parameters include all TX EQ, RX CTFFEE PRE1 and PRE2 (no post yet), CTLE DC, LF, HF, BW,
##   Timing Veneer Edge, up_eye, mid_eye, low_eye
## - Modified output name to include data rate and channel description
## - Modified outputs names to match Avago Required Register Names
## 
## Version 2.0 9/30/2015 CAP
## Add support for Simba Test Chip (16nm NRZ)
##
##
##
##
require 'csv'

def sweep2(rx_addr=6)
	
	#############################################################
	#           LOAD CONFIG FILE AND PARSE
	#############################################################

	# Load the Config Sweep file
	conf=CSV.parse(File.read("./sweep/Config_sweep.csv"))

	width_mode=80

	# Parse Config File and assign sweep values to each Variable
	# Format of csv
	# column 0: reg name  column 1: start value   column 2: end value  column 3: step size (step size must be 1 or more)
	len=(conf.length)
	#puts len

	x=0
	while x < len
		#check for empty lines which get a value of NIL another complex Ruby Issue
		if conf[x].nil? == false
			key=conf[x][0]
			case key
				when "tx_pre"
					txpre=conf[x]
				when "tx_post"
					txpost=conf[x]
				when "tx_atten"
					txatten=conf[x]
				when "rxaddr"
					rx_addr= (conf[x][1]).to_i(10)
				when "loops"
					loops = (conf[x][1]).to_i(10)
				when "rx_dc"
					rxdc=conf[x]
				when "rx_lf"
					rxlf=conf[x]
				when "rx_hf"
					rxhf=conf[x]
				when "rx_bw"
					rxbw=conf[x]
				when "Pattern"
					patt = (conf[x][1]).to_s
				when "Datarate"
					drate_ghz = (conf[x][1]).to_f
				#when "ctle_ena"
				#	ctle_ena= (conf[x][1]).to_i(10)
				#when "ctffe_ena"
				#	ctffe_ena= (conf[x][1]).to_i(10)
				when "iCal"
					ical= (conf[x][1]).to_i(10)
				when "pCal"
					pcal= (conf[x][1]).to_i(10)	
				when "delCal"
					delcal= (conf[x][1]).to_i(10)	
				when "piCal"
					pical= (conf[x][1]).to_i(10)								
				when "fixed_bw"
					fixed_bw= (conf[x][1]).to_i(10)
				when "fixed_dc"
					fixed_dc= (conf[x][1]).to_i(10)
				when "fixed_hf"
					fixed_hf= (conf[x][1]).to_i(10)
				when "fixed_lf"
					fixed_lf= (conf[x][1]).to_i(10)
				when "ber_dwell"
					dwell= (conf[x][1]).to_f
				when "Channel"
					chan= (conf[x][1])
				when "init"
					init = (conf[x][1]).to_i(10)
				when "firmware"
					firmwr=(conf[x][1]).to_s
				when "Divider"
					div = (conf[x][1]).to_i(10)
				#when "pulse_en"
				#	pulse_en= (conf[x][1]).to_i(10)
				when "eye_en"
					eye_en= (conf[x][1]).to_i(10)
				else
					z=1
					#puts "ignore line"
			end # case
		end # if 
		x+=1
	end # while
	#puts len
	
	# get serdes type
	serdes_type = system.server.chip0.sbus_ring.get_device_by_address(rx_addr).get_serdes_type

	# instantiate the serdes object as r
	r = system.server.chip0.sbus_ring.get_device_by_address(rx_addr); extend_serdes_object(r)
	
	# create file name
	time1=Time.new
	yr=time1.year.to_s
	month= time1.month.to_s
	day = time1.day.to_s
	hour= time1.hour.to_s
	min = time1.min.to_s
	drates= drate_ghz.to_s
	fname = "./sweep/sweep_" + chan + "_" + drates + "gbps_" + month + "_" + day + "_" + yr + "_" + hour +"_" + min + ".csv"
	
	# calculate total loops
	rangelist = []
	totloops=1
	
	# put all reglists into a big list
	reglist=[txpre, txpost, txatten]
	if fixed_dc==1
		reglist << rxdc
	end
	if fixed_lf==1
		reglist << rxlf
	end
	if fixed_hf==1
		reglist << rxhf
	end
	if fixed_bw==1
		reglist << rxbw
	end
	

	# calculate range and store in rangelist
	reglist.each {|setlist| rangelist << (setlist[2].to_i-setlist[1].to_i)/setlist[3].to_i}
	
	# ignore 0s and calculate total loops
	rangelist.each {|range| 
			        if range !=0
						totloops=totloops * (range+1)
					end}
	totloops=totloops * loops
	#fixme fixed_lf/hf/dc/bw are on then the range shoud lbe ignored
	puts "We will run a total of #{totloops} loops"

	#create header for logfile. Each paraneter will have a column in the final CSV file
	header = ['loop','DRate Gbps','Pattern','Channel','TXpre', 'TXpost', 'TXattn','vos0','vos1','vos2','vos3','vos4','vos5','vos06','vos07',
	'dc','lf','hf','bw','gain','tap1','tap2','tap3','tap4','tap5','tap6','tap7','tap8','tap9','tapA','tapB','tapC','tapD','errors',
	'BER@eh0V','eh@1e10','eh@1e12','eh@1e15','eh@1e17','eh_r2fit', 'BER@ew0mUI', 'ew@1e10', 'ew@1e12', 'ew@1e15', 'ew@1e17', 'ew_r2fit']
	CSV.open(fname, 'w') do |wrt|
		wrt << header
	end
	
    #############################################################
	#           MAIN LOOP
	#############################################################
	
	loop=1
	## Init all Registers to Start Values
	txpst= txpost[1].to_i
	while txpst < txpost[2].to_i+1
		txp= txpre[1].to_i
		while txp < txpre[2].to_i+1
					txattn= txatten[1].to_i
					while txattn < txatten[2].to_i+1
											rx_dc=rxdc[1].to_i
											while rx_dc < rxdc[2].to_i+1
											rx_dc_offset=rx_dc<<2 #hack because broken in AAPL, filed redmine #4725
												rx_lf=rxlf[1].to_i
												while rx_lf < rxlf[2].to_i+1
													rx_hf=rxhf[1].to_i
													while rx_hf < rxhf[2].to_i+1
														rx_bw=rxbw[1].to_i
														while rx_bw < rxbw[2].to_i+1
															iloop=1
															while iloop < loops+1
															
															#fixme could add how much time we think is left
															puts""
															puts "Running Loop #{loop} of #{totloops} with TXpost= #{txpst}; TXpre= #{txp}"
															#puts"atten=#{txattn}, rx_dc=#{rx_dc}, rx_dc_offset=#{rx_dc_offset}, rx_lf=#{rx_lf}, rx_hf=#{rx_hf}, rx_bw=#{rx_bw}, iloop=#{iloop}"
															
																if init == 1
																	#define firmware file including full path
																	 fw_win_path="./Firmware/"+firmwr

																	  # upload Firmware
																	  r.upload_spico :ram_bist => true, :path => fw_win_path 

																	  #init serdes for ILB with prbs31
																	  width_mode = 40
																	  r.serdes_init :tx_div=> div, :tx_width=> width_mode, :rx_div=> div, :rx_width=> width_mode, :init_mode=> :prbs31_ilb
																	   
																end
												
																 
																############
																#set to ELB
																############
																r.set_rx_input_loopback(select_internal=false)
																puts "putting serdes in ELB"	  
																r.aapl.avago_spico_int r.address, 0x0003, 0x0203 # main -vs- patgen
															    sleep (0.05)
																r.set_tx_rx_pat(patt) #cmp_data 
																#r.set_rx_term(term=:avdd)
												
																### Set Tx EQ ###
																r.set_d6_tx_eq(pre=txp,post=txpst,atten=txattn) 
																printf("setting Tx EQ pre:%d post:%d atten:%d \n",txp,txpst,txattn)
                
																### disable electrical idle until bug is fixed ###
																printf("Disable signal_ok \n")
																r.aapl.avago_spico_int r.address, 0x20, 0x0 # disable Electrical Idle  
																sleep (0.1)
																
																#############################################
																# Setting fixed DFE settings and tuning mode
																#############################################
																
																tuning_mode=0x0 #define a variable to define the tuning mode according to fixed_lf/hf/dc/bw
															
																if (pcal == 0)
																r.aapl.avago_spico_int r.address, 0x26, 0x5B01  # disable auto-pCal
																end
																
																if fixed_dc==1
																	puts " setting fixed DC = #{rx_dc}"
																	r.aapl.avago_spico_int rx_addr, 0x26, 0x2200 | rx_dc_offset # set dc	
																	tuning_mode=tuning_mode|0x0080 #add fixed_dc to tuning mode
																end
												
																if fixed_lf==1
																	puts "setting fixed CTLE LF = #{rx_lf}"
																	r.aapl.avago_spico_int rx_addr, 0x26, 0x2100 | rx_lf # set LF
																	tuning_mode=tuning_mode|0x0100 #add fixed_lf to tuning mode
																end
																
																if fixed_hf==1
																	puts "setting fixed CTLE HF = #{rx_hf}"
																	r.aapl.avago_spico_int rx_addr, 0x26, 0x2000 | rx_hf # set HF
																	tuning_mode=tuning_mode|0x0200 #add fixed_hf to tuning mode
																end
																
																if fixed_bw==1
																	puts "setting fixed CTLE BW = #{rx_bw}"
																	r.aapl.avago_spico_int rx_addr, 0x26, 0x2300 | rx_bw # set BW
																	tuning_mode=tuning_mode|0x0400 #add fixed_bw to tuning mode
																end
																
																# force to exit the loop if fixed_xx is not chosen
																
																if fixed_dc==0																	
																rx_dc=rxdc[2].to_i #set to the max range to force out of the DC loop
																end
																
																if fixed_hf==0
																	rx_hf=rxhf[2].to_i #set to the max range to force out of the hf loop
																end
															
																if fixed_lf==0
																	rx_lf=rxlf[2].to_i #set to the max range to force out of the lf loop
																end
																
																if fixed_bw==0
																	rx_bw=rxbw[2].to_i #set to the max range to force out of the BW loop
																end
																
																###############
																#Tuning Rx-EQ
																###############
																
																printf("tuning Rx on sbus: 0x%x \n",rx_addr)
																
																if (ical==1)
																puts"running iCal ... "
																  #r.aapl.avago_spico_int r.address, 0x0A, 0x0781 # iCal + tuning mode defined above
																  r.aapl.avago_spico_int r.address, 0x0A, tuning_mode|0X0001 # iCal + tuning mode defined above
																  #fixme dfe_wait doesnt exist in ascript
																  #r.avago_serdes_dfe_wait
																  tunetime=r.rx_tune_wait(timeout=400)
																end
																
																if (pcal==1)
																puts"running pCal ... "
																  r.aapl.avago_spico_int r.address, 0x0A, tuning_mode|0x0002 # one shot pCal + tuning mode defined above
																  #fixme dfe_wait doesnt exist in ascript
																  #r.avago_dfe_wait
																  tunetime= r.rx_tune_wait(timeout=400)
																end
												  
																#fixme need to call the aapl delay_cal function. Issue with eye diagram not being valid even after delay cal (not PI cal)
																#if (delcal == 1)
																#  r.aapl.avago_spico_int r.address, 0x0003, 0x0203 # main -vs- patgen
																#  delCal = r.delay_cal_16nm     # choose best edge/data RSA vernier
																#  pi_cal_array = r.delay_cal(mode=0,dwell=1000000000) # aapl version of vernier phase calibration
																#else
																#  delCal = 999
																#end

																#if (pical == 1)
																#  r.aapl.avago_spico_int r.address, 0x0003, 0x0203 # main -vs- patgen
																#  pi_cal_array = r.delay_cal(mode=0,dwell=1000000000) # aapl version of phase interpolator calibration
																#else
																#  pi_cal_array = [999,999,999]
																#end
												 
																###################
																# ERROR COUNTING  #
																###################
												      		
																#put the counter back into proper mode (cmsp+mode main_PatGen, cmp_data PRBSx)
																r.aapl.avago_spico_int rx_addr, 0x0003, 0x0203 # main -vs- patgen
																#r.set_tx_rx_pat(patt)

																#fixme this is where we count errors in elb
																aapl.avago_spico_int rx_addr, 0x017, 0x0000 # reset error counter
																#r.set_rx_cmp_data(input=patt)
																errors=r.get_sample_errors(samples="1M")
																printf("We detected %d errors after 1M bits ...\n", errors)
											
																#r.aapl.avago_spico_int rx_addr, 0x0003, 0x0203 # main -vs- patgen	
											
																###################################
																# Gather results
																###################################
														
																### Get Rx EQ parameters ###
																dfedump = r.get_rx_state
													
																# puts"get vbtc data"
																hbtc_1, vbtc_1=r.get_hvbtc(rx_addr) # horizontal / vertical bathtub curv info, by Liang Li @ Cisco
																
																puts "Extrapolated Eye height at 1e-10 BER = #{vbtc_1.vert_eye_1e10} mV"
																puts "Extrapolated Eye width at 1e-10 BER = #{hbtc_1.horz_eye_1e10} mUI"
																# puts hbtc_1

																# Eye Diagram .ebert file
																if eye_en == 1
																    puts"gathering eye diagram ..."
																	filename=".\\rx_eyes\\sweep_" + chan + "_" + drates.to_i.to_s + "Gbps_" + txattn.to_s + txp.to_s + txpst.to_s + "_" + iloop.to_s + "_" + "eye_data.ebert"
																	# filename="./rx_eyes/sweep_" + chan + "_" + drates + "gbps_" + month + "_" + day + "_" + yr + "_" + hour +"_" + min + "eye_data.ebert"
																	#fixme write_eye doesnt exist for D6
																	#fixme be careful the line below dumps eye with wrong settings cmp_data = XOR and qual=default 
																	r.write_eye_btc_file(rx_addr, filename)
									
																end
																
																# This is for escope option
																#if pulse_en == 1
																#	  filename="./rx_eyes/sweep_" + chan + "_"+drates+"gbps"+"_" + "pulse_data.csv"
																#	  pattp="PRBS7"
																#	  r.set_tx_rx_pat(pattp)
																#	  r.write_escope_file(rx_addr, filename)
																#	  #set pattern back to prbs in config file
																#	  r.set_tx_rx_pat(patt)
																 #end
																
																###################################
																# Dump all Values
																###################################
													
																#puts "Define output line"
																curline=[loop,drate_ghz,patt,chan,txp,txpst,txattn]
																
																#puts "append dfedump values to curline"
																dfedump.each {|regval| curline << regval}

																#error count
																curline << errors
																
																# vbtc info
																curline << vbtc_1.vert_ber_0mV
																curline << vbtc_1.vert_eye_1e10
																curline << vbtc_1.vert_eye_1e12
																curline << vbtc_1.vert_eye_1e15
																curline << vbtc_1.vert_eye_1e17
																curline << vbtc_1.bottom_R_squared #measurement confidence (should be really close to 1)

																# hbtc info
																curline << hbtc_1.horz_ber_0mUI
																curline << hbtc_1.horz_eye_1e10
																curline << hbtc_1.horz_eye_1e12
																curline << hbtc_1.horz_eye_1e15
																curline << hbtc_1.horz_eye_1e17
																curline << hbtc_1.left_R_squared #measurement confidence (should be really close to 1)

																# open Output File in append mode
																CSV.open(fname, 'a') do |wrt|
																	wrt << curline  
																end
																
																loop +=1
																iloop +=1
																
															end # 
															rx_bw = rx_bw + rxbw[3].to_i
														end
														rx_hf= rx_hf + rxhf[3].to_i
													end
													rx_lf= rx_lf + rxlf[3].to_i
												end	
												rx_dc= rx_dc + rxdc[3].to_i
						end
						txattn = txattn + txatten[3].to_i
			end
			txp = txp + txpre[3].to_i
		end
		txpst = txpst + txpost[3].to_i
	end

end




		






