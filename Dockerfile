FROM ramadhani892/ramubot:dragons

RUN git clone -b master https://github.com/zarszs/RAM-UTOD home/master/ 
   
WORKDIR /home/master/

CMD ["python3", "-m", "rams"]
