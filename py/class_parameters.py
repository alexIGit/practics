 
class Any():
	glob_param = [1, 2, 3]

	def __init__(self, local='local'):
		self.loc_param = [10, 20, 30]


if __name__ == '__main__':

	one = Any()
	two = Any()


	print(f"one glob: {one.glob_param} == {two.glob_param} :glob two")
	one.glob_param.append('11111')
	two.glob_param.append('22222')
	print(f"one glob: {one.glob_param} == {two.glob_param} :glob two")


	print(f"one local: {one.loc_param} == {two.loc_param} :local two")
	one.loc_param.append('1111')
	two.loc_param.append('2222')
	print(f"one local: {one.loc_param} is not {two.loc_param} :local two")