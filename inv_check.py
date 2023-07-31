import csv


global_arr = []
not_found = []

#in the future use mutli threading, so that you can scan, and await user input for save or cancel

def write_csv(global_arr, not_found):
	with open('out_put.csv', 'w+', newline='') as write_csvfile:
		write_csv = csv.writer(write_csvfile, delimiter=' ',quotechar='|')
		for row in global_arr:
			row = ','.join(row)
			write_csv.writerow([row])



		not_found = ','.join(not_found)
		write_csv.writerow(['Asset Numbers not in Inventory,' + not_found])
			


def read_csv(global_arr):
	with open('Untitled spreadsheet - Sheet1.csv', newline='') as read_csvfile:
		read_cvs_file = csv.reader(read_csvfile, delimiter=' ',quotechar='|')
		for row in read_cvs_file:
			check = row[0].split(',')
			global_arr += [check]



def check_asset(global_arr, asset_tag, not_found):
	for cell in global_arr:
		if cell[1] == asset_tag:
			cell.append('Found in Inventory')
			print('Found in Inventory \n')
			return 0

	print('not found\n')
	not_found += [asset_tag]





def main(global_arr, not_found):
	read_csv(global_arr)
	print("Scan Asset -or- Type: Done")
	while(True):
		option = input()
		if option == 'Done':
			write_csv(global_arr, not_found)
			print("Assets are updated in out_put.csv")
			break
		else:
			check_asset(global_arr, option, not_found)


main(global_arr, not_found)




