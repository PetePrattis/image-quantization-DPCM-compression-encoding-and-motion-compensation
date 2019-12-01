clc;

close all;

clear all;

import VideoReader;
%reading a video file

mov = VideoReader('C:/path/airplane.MOV');

t=1;
for i=1:30
  currFrame = read(mov,t);
  currFrame = imrotate(currFrame,270);
  currFrame = rgb2gray(currFrame);
  base_file_name = sprintf('%d.png',t);
  full_file_name = fullfile('C:\Users\path\',base_file_name);
  
  imwrite(currFrame,full_file_name,'png');
  t=t+1;
  
  end
  
video = VideoWriter('compressed.avi'); %create the video object
video2=VideoWriter('gray_video_with_30frames.avi');
open(video); %open the file for writing
open(video2);

writeVideo(video,imread('1.png'));

for j=1:30 
writeVideo(video2,imread(sprintf('%d.png',j)));
end
close(video2);

for j=2:30 %video neo
  image_now = imread(sprintf('%d.png',j));
  image_before = imread(sprintf('%d.png',j-1));
  
  errorblock = image_now - image_before;
  quantization = errorblock /20;
  image_now = image_before + quantization;
  writeVideo(video,image_now);
end


%for j=2:30
%image_now = imread(sprintf('%d.png',j));
%errorblock = imread(sprintf('%d.png',j-1));
%diff = image_now - errorblock/10;
%q_diff = diff +10;
%image_now =  errorblock + q_diff;
%errorblock = image_now +10;
%writeVideo(video,image_now);
%end;

close(video);  
