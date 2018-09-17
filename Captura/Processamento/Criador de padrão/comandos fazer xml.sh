#!/bin/bash

opencv_createsamples -img cat.jpg -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 35


opencv_createsamples -info info/info.lst -num 35 -w 20 -h 20 -vec positives.vec


opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1 -numNeg 35 -numStages 30 -w 20  -h 20 -featureType LBP

echo "Processamento Finalizado"