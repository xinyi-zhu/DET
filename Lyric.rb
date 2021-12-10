# Welcome to Sonic Pi

instruments = [:piano, :sine, :pluck]
amplitute = [0.5, 0.8, 1]

live_loop :foo do
  
  use_real_time
  
  input = sync "/osc*/play_this"
  
  note = input[0]
  ins = instruments[input[1]]
  amp = amplitute[input[2]]
  
  use_synth ins
  play_pattern_timed chord(note, :major, num_octaves:1), 0.125, release: 0.5, amp: amp
  sleep 0.125
  
end