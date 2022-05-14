# @param {String} s
# @return {Integer}
def roman_to_int(s)

  roman_map = {
    :I=> 1, :V=> 5, :X => 10 , :L => 50 , :C=> 100, :D => 500, :M =>1000
  }

  # roman_map.each do |key, value|
  #   puts value
  # end

  input = s.reverse.split('')
  current_ans = 0

  input.each do |c|
    #converting to symbol
    c = c.to_sym
    # Check if the key exists in the hash
    if roman_map.has_key?c
      # Check if it it should be subtracted
      if roman_map[c]*4 < current_ans
        current_ans = current_ans-roman_map[c]
      #else just add it to the answer
      else
        current_ans =current_ans + roman_map[c]
      end
    else

    end
  end

  current_ans




end


puts roman_to_int("MXXIII")
