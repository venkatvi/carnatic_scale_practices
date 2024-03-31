""" TODO: Add more documentation and CLI parameterization of new scales""" 
from typing import Dict, List
SARALI_VARISAIS = [
	["srgmpdnS", "Sndpmgrs"], 
	["srsrsrgm", "srgmpdnS", "SnSnSndp", "Sndpmgrs"], 
	["srgsrgsr", "srgmpdnS", "SndSndSn", "Sndpmgrs"], 
	["srgmsrgm", "srgmpdnS", "SndpSndp", "Sndpmgrs"], 
	["srgmp,sr", "srgmpdnS", "Sndpm,Sn", "Sndpmgrs"], 
	["srgmpdsr", "srgmpdnS", "SndpmgSn", "Sndpmgrs"], 
	["srgmpdn,", "srgmpdnS", "Sndpmgr,", "Sndpmgrs"],
	["srgmpmgr", "srgmpdnS", "Sndpmpdn", "Sndpmgrs"],
	["srgmpmdp", "srgmpdnS", "Sndpmpgm", "Sndpmgrs"], 
	["srgmp,gm", "p,,,p,,,", "gmpdndpm", "gmpgmgrs"], 
	["S,ndn,dp", "d,pmp,p,", "gmpdndpm", "gmpgmgrs"],
	["SSndnndp", "ddpmp,p,", "gmpdndpm", "gmpgmgrs"],
	["srgrg,gm", "pmp,dpd,", "mpdpdndp", "mpdpmgrs"],
	["srgmp,p,", "ddp,mmp,", "dnS,Sndp", "Sndpmgrs"],
]
COMMA_POSITION = 1000
THALA_BREAK = 4
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
	decoded_varisais = convert_to_different_scale(["srgmpdnS", "Sndpmgrs"], ["srgpdSRG", "GRSdpgrs"], SARALI_VARISAIS, "sarali_varisai")
	for idx, varisai_lines in enumerate(decoded_varisais): 
		print(f"Lesson {idx+1}\n")
		for line in varisai_lines: 
			print(line[:THALA_BREAK] + "|" +  line[THALA_BREAK :] + "||\n")
		print("---------------------------------")