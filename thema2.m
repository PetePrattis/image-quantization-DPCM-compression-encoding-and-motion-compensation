clc;

close all;

clear all;

import VideoReader;
%reading a video file

mov = VideoReader('C:/Users/Panagiotis Prattis/Desktop/matlabtests/airplane.MOV');

t=1;
for i=1:30
  currFrame = read(mov,t);
  currFrame = imrotate(currFrame,270);
  currFrame = rgb2gray(currFrame);
  base_file_name = sprintf('%d.png',t);
  full_file_name = fullfile('C:\Users\Panagiotis Prattis\Desktop\matlabtests\',base_file_name);
  
  imwrite(currFrame,full_file_name,'png');
  t=t+1;
  
  end
  
video = VideoWriter('compressed.avi'); %create the video object
video2=VideoWriter('gray_video_with_30frames.avi');
open(video); %open the file for writing
open(video2);

writeVideo(video,imread('1.png')); %1o erwthma

for j=1:30 %gia na doume posa mb einai to arxiko video se gray apoxrwseis
writeVideo(video2,imread(sprintf('%d.png',j)));
end
close(video2);

for j=2:30 %video neo
  image_twra = imread(sprintf('%d.png',j));
 image_prin = imread(sprintf('%d.png',j-1));
  
  sfalma = image_twra - image_prin;
  kvantisi = sfalma /20;
  image_twra = image_prin + kvantisi;
  writeVideo(video,image_twra);
end


%for j=2:30
%image_twra = imread(sprintf('%d.png',j));
%sfalma = imread(sprintf('%d.png',j-1));
%diafora = image_twra - sfalma/10;
%q_diafora = diafora +10;
%image_twra =  sfalma + q_diafora;
%sfalma = image_twra +10;
%writeVideo(video,image_twra);
%end;

close(video);  