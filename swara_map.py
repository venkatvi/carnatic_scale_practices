""" TODO: Add more documentation and CLI parameterization of new scales""" 
from typing import Dict, List
from ragams import DEFAULT, SUDDHA_SAVERI
from varisais import SARALI_VARISAIS, DHATTU_VARISAIS, THALA_BREAK, COMMA_POSITION
def get_swara_to_position_map(scale: List[str]) -> Dict[str, int]: 
	#assert(len(scale) == 2, "scale should have strictly 2 strings")
	aarohanam = scale[0]
	avarohanam = scale[1]
	scale_map = {}
	for idx, c in enumerate(aarohanam): 
		scale_map[c] = idx 

	# for idx, c in enumerate(avarohanam): 
	# 	assert(scale_map[c] == idx, "Scales should be symmetric")
	return scale_map

def get_position_to_swara_map(scale: List[str]) -> Dict[str, int]: 
	#assert(len(scale) == 2, "scale should have strictly 2 strings")
	aarohanam = scale[0]
	avarohanam = scale[1]
	scale_map = {}
	for idx, c in enumerate(aarohanam): 
		scale_map[idx] = c 

	# for idx, c in enumerate(avarohanam): 
	# 	assert(scale_map[idx] == c, "Scales should be symmetric")
	return scale_map

def convert_to_different_scale(
	original_scale: List[str], 
	new_scale: List[str],
	varisais: List[List[str]],
	varisai_string: str 
) -> List[List[str]]: 
	print(f"Converting {varisai_string} from {original_scale} to {new_scale}")
	original_map = get_swara_to_position_map(original_scale)

	encoded_varisais: List[List[List[int]]] = []
	for varisai in varisais:
		encoded_lines = []
		for line in varisai: 
			varisai_positionS = []
			for c in line:
				#assert(c in original_map, "Invalid swara {} in varisai {}".format(c, line ))
				if c in original_map.keys(): 
					varisai_positionS.append(original_map[c])
				else: 
					varisai_positionS.append(COMMA_POSITION)
			encoded_lines.append(varisai_positionS)
		encoded_varisais.append(encoded_lines)


	new_map = get_position_to_swara_map(new_scale)

	decoded_varisais = [] 
	for encoded_varisai in encoded_varisais: 
		decoded_varisai = [] 
		for encoded_line in encoded_varisai: 
			decoded_string = ""
			for pos in encoded_line: 
				#assert(pos in new_map, "Invalid position {} in varisai {}". format(pos, encoded_line))
				if pos in new_map.keys(): 
					decoded_string += new_map[pos]
				elif pos == COMMA_POSITION: 
					decoded_string +=","
			decoded_varisai.append(decoded_string)
		decoded_varisais.append(decoded_varisai)

	return decoded_varisais

if __name__ == "__main__": 
	varisais = DHATTU_VARISAIS
	conversion_name = "dhattu varisais"
	decoded_varisais = convert_to_different_scale(DEFAULT, SUDDHA_SAVERI, varisais, conversion_name)
	for idx, varisai_lines in enumerate(decoded_varisais): 
		print(f"Lesson {idx+1}\n")
		for line in varisai_lines:
			start = 0
			end = 0
			modified_line = "" 
			for thala in THALA_BREAK: 
				end = end + thala
				modified_line += line[start:end] 
				modified_line += "|" 
				start = end
			modified_line += "|"
			print(modified_line + "\n")
		print("---------------------------------")