import os
#from shutil import copyfile
import shutil

if __name__ == "__main__":
	filesizeOffset = 400 * 1024
	appdataPath = 'C:\\Users\\virajkumar.patel\\AppData'
	spotlightPath = '\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets'

	#Add local disk path here LOCAL_PATH
	# Example : C:\\Users\\john.doe\\Desktop\\HDWallpapers
	localpath = 'C:\\Users\\virajkumar.patel\\Desktop\\HDWallpapers'
	toDirPath = ""

	if localpath.endswith("\\"):
		toDirPath = localpath + "spotlightdownloads"
	else:
		toDirPath = localpath + "\\spotlightdownloads"

	if os.path.exists(toDirPath):
		shutil.rmtree(toDirPath)
	else:
		os.makedirs(toDirPath)
	assetsPath = appdataPath + spotlightPath
	allfiles = os.listdir(assetsPath)

	fileCopiedCount = 0

	for file in allfiles:
		filepath = assetsPath + "\\"+ file
		filesize = os.path.getsize(filepath)
		if filesize > filesizeOffset:
			#print ('filesize of file "' + file + '" is ' + str(filesize) + " bytes")
			distPath = toDirPath + "\\" + file + ".jpg"
			shutil.copyfile(filepath,distPath)
			fileCopiedCount += 1

	if(fileCopiedCount > 0):
		print(str(fileCopiedCount) + ' files downloaded successfully.')
		print('"In only c<>de we trust."')
	else:
		print('Oh, Snap! Wait for good stuff...')
