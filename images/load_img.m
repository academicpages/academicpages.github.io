a = imread('profile1.png');
a1 = a(421:920,551:1050,:);
a1 = imresize(a1,[700,700],'bicubic');
imshow(a1)