echo cmd.bat path : %~dp0
dir    %~dp0\*.proto /B > protoNames.txt              

for  /f  %%a  in  (protoNames.txt)  do (
	echo %%a
	protoc --proto_path= --python_out=../../model %%a
)
     pause