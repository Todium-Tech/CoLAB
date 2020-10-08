from google.colab import files,drive

# Uploading files from your local file system
# files.upload returns a dictionary of the files which were uploaded. 
# The dictionary is keyed by the file name and values are the 
# data which were uploaded.

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))


# Downloading files to your local file system
# files.download will invoke a browser download of the file to your local computer.

with open('example.txt', 'w') as f:
  f.write('some content')

files.download('example.txt')



# Google Drive  
# Mounting Google Drive Locally

drive.mount('/content/drive')

with open('/content/drive/My Drive/foo.txt', 'w') as f:
  f.write('Hello Google Drive!')

drive.flush_and_unmount()
print('All changes made in this colab session should now be visible in Drive.')





