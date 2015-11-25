Log.info "Loading #{__FILE__}"

$WORKSPACE_ROOT = File.join "../", File.dirname(__FILE__)
$WORKSPACE_TARGET = "/coral"
$FILEPATH_PLOT = Dir.pwd + '/rx_eyes/'

$LOAD_PATH << $WORKSPACE_ROOT
$LOAD_PATH << $WORKSPACE_ROOT + $WORKSPACE_TARGET


def extend_serdes_object(serdes_object)

  @serdes=serdes_object

  if Ascript::Control::SerdesCharLab.const_defined?(:"SerdesControl_#{serdes_object.get_serdes_type}")

    @serdes.extend Ascript::Control::SerdesCharLab.const_get "SerdesControl_#{serdes_object.get_serdes_type}"

  end

end


##########################################################################################
# The user_require and reload methods work together and are used for development.  If
# a file is being required with the user_require method, it will be reloaded when the 
# reload method is called from the interactive command prompt.  Any file required using
# only require, it will not be reloaded.
def user_require(path)
  Log.info "Loading user required file #{path}"
  $USER_REQUIRES ||= []
  $USER_REQUIRES << path
  begin
    Kernel.require path
  rescue LoadError
    Log.error "Can't find user required file '#{path}'"
    false
  end
end

def reload
  valid = true
  $USER_REQUIRES.each do |ur|

    paths = $LOAD_PATH.map {|lp| [File.join(lp, ur), File.join(lp, "#{ur}.rb")] }.flatten
    path = paths.reverse.find {|p| File.exists? p}

    if path.nil?
      Log.error "Can't find user required file '#{ur}'"
      valid = false
    else
      Log.info "Loading #{path}"
      load path
    end
  end
  valid
end
##########################################################################################


# add plugins
Ascript::Plugins.path = "./plugins"
Ascript::Plugins.setup

require "mapfiles"

# SerDes Control
user_require 'SerdesControl_sd16C_txhs_rxd6_ns_02'

# Init Scripts 
user_require 'sweep_2_0.rb'

def extend_serdes_object(serdes_object)
  @serdes=serdes_object
  if Ascript::Control::SerdesCharLab.const_defined?(:"SerdesControl_#{serdes_object.get_serdes_type}")
    @serdes.extend Ascript::Control::SerdesCharLab.const_get "SerdesControl_#{serdes_object.get_serdes_type}"
  end
end

