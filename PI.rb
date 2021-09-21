##| # Welcome to Sonic Pi

##| live_loop :drums do
##|   sample :drum_heavy_kick
##|   sleep 1
##| end

##| 2.times do
##|   play_pattern_timed [:E5, :Eb5], [0.25]
##| end
##| play_pattern_timed [:e5, :b4, :d5, :c5], [0.5]
##| play :a4
##| sleep 1


##| play_pattern_timed chord(:c4, :major, num_octaves:1), 0.125, release: 0.1
##| play (chord :c, :major).choose

##| live_loop :arp do
##|   play (scale 60, :minor_pentatonic).tick, release: 0.1
##|   sleep 0.125
##| end



##| live_loop :foo do

##|   use_real_time
##|   fruit = sync "/osc*/play_fruit"
##|   synth :mod_sine, note: fruit[0],amp:0.5

##|   vegetable = sync "/osc*/play_vegetable"
##|   synth :kalimba, note: vegetable[0],amp:1

##|   snack = sync "/osc*/play_snack"
##|   synth :dull_bell, note: snack[0],amp:0.5

##|   sleep 0.125

##| end


broccoli = [:F4, :AB4, :c5, :mod_sine]
carrot = [:D4, :Gb4, :A4, :mod_sine]
banana = [:E4, :Ab4, :B4, :kamilba]
orange = [:D4, :Gb4, :A4, :kamilba]
apple = [:c4, :e4, :g4, :kamilba]
donut = [:D4, :Gb4, :A4, :dull_bell]
cake = [:B4, :D5, :Gb5, :dull_bell]
hotdog = [:c4, :e4, :g4, :dull_bell]

live_loop :foo do
  
  use_real_time
  
  play (chord :c, :major).choose
  
  input = sync "/osc*/play_this"
  
  case input[0]
  when 1
    use_synth banana[3]
    play banana[0]
    sleep 0.25
    play banana[1]
    sleep 0.25
    play banana[2]
    sleep 0.25
  when 2
    use_synth apple[3]
    play apple[0]
    sleep 0.25
    play apple[1]
    sleep 0.25
    play apple[2]
    sleep 0.25
  when 3
    use_synth orange[3]
    play orange[0]
    sleep 0.25
    play orange[1]
    sleep 0.25
    play orange[2]
    sleep 0.25
  when 4
    use_synth broccoli[3]
    play broccoli[0]
    sleep 0.25
    play broccoli[1]
    sleep 0.25
    play broccoli[2]
    sleep 0.25
  when 5
    use_synth carrot[3]
    play carrot[0]
    sleep 0.25
    play carrot[1]
    sleep 0.25
    play carrot[2]
    sleep 0.25
  when 6
    use_synth donut[3]
    play donut[0]
    sleep 0.25
    play donut[1]
    sleep 0.25
    play donut[2]
    sleep 0.25
  when 7
    use_synth cake[3]
    play cake[0]
    sleep 0.25
    play cake[1]
    sleep 0.25
    play cake[2]
    sleep 0.25
  else
    use_synth hotdog[3]
    play hotdog[0]
    sleep 0.25
    play hotdog[1]
    sleep 0.25
    play hotdog[2]
    sleep 0.25
  end
  
  sleep 0.5
  
end


