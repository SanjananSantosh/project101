import os
import dropbox

class TransferingData:
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            for filename in files:
                path = os.path.join(root,filename)
                relative_path=os.path.relpath( path,file_from)
                dropbox_path=os.path.join(file_to,relative_join)
                with open( path,'rb')as f:
                    dbx.files.upload(f.read(),dropbox_path,mode=writemode('overwrite'))

def main():
    access_token='sl.Av-VirrXAyQT0bWDg_mA6uLVAIxzn3rdtqr9ooDolQKWIZAREX2QP-POSHxelzd5vLyClKLa4w_g1Ksxqz3xu7gi22Ny4oXNRsxl5mpWpdT9CHXrMV_ANmKpT9fyXQK5zaDdolQ'
    transferingData=TransferingData(access_token)
    file_from = input("Enter the folder path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")
    transferingData.upload_file(file_from, file_to)
    print("File is uploaded succesfully!!!")
    
    
main()