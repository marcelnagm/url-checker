# url-checker

You can acquire all url of you website by using pylinkvalidate.py


eg:
  ./pylinkvalidate.py [website]-P -w 500  --format=plain  --output=./list.bk > op.txt
  
  then use the list to ensure that all url are ok by url_checker
  
  eg 
   python3 url_checker.py  file > file-result.txt
   
   then to filter use this command
   
   cat 'result.txt' | awk '$0 ~ /Status: 404/' >> notfoud.txt 

