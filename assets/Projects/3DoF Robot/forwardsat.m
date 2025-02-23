syms t1 t2 t3 t4 t5

% measurement in cm

R01x = [cos(t1) -sin(t1) 0;
        sin(t1) cos(t1) 0;
        0 0 1];
R01y = [1 0 0;
        0 0 -1;
        0 1 0];
R01= R01x*R01y
%
R23x = [cos(t3) -sin(t3) 0;
        sin(t3) cos(t3) 0;
        0 0 1];
R23y = [0 0 1;
        1 0 0;
        0 1 0];
R23= R23x*R23y
%
R34x = [cos(t4) -sin(t4) 0;
        sin(t4) cos(t4) 0;
        0 0 1];
R34y = [1 0 0;
        0 0 1;
        0 -1 0];
R34= R34x*R34y
%
R45x = [cos(t5) -sin(t5) 0;
        sin(t5) cos(t5) 0;
        0 0 1];
R45y = [0 1 0;
        -1 0 0;
        0 0 1];
R45= R45x*R45y

%%
%EGR 455
%Project
% R⊥R//R⊥R⊥R

syms t1 t2 t2 t3 t4 t5
a1 = 10
a2 = 13
 a3 = 10
 a4 = 3
 a5 = 10



% t1 = (0)*pi/180
% t2 = (120)*pi/180
% t3 = (270)*pi/180
% t4 = (0)*pi/180
% % t5 = (270)*pi/180
% 
t1 = (0)*pi/180
t2 = (0)*pi/180
t3 = (0)*pi/180
t4 = (0)*pi/180
t5 = (0)*pi/180

H01 = [cos(t1) 0 sin(t1) 0;...
       sin(t1) 0 -cos(t1) 0;...
       0        1   0      a1;...
       0        0   0       1]
   
H12 = [cos(t2) -sin(t2) 0 a2*cos(t2);...
       sin(t2) cos(t2) 0 a2*sin(t2);...
       0        0      1    0;...
       0        0       0   1]
   
H23 = [-sin(t3) 0 cos(t3) 0;...
       cos(t3) 0 sin(t3) 0;...
       0 1 0 0;...
       0   0       0      1]
   
H34 = [cos(t4) 0 -sin(t4) 0;...
       sin(t4) 0 cos(t4) 0;...
       0  -1 0 a3+a4;...
       0 0 0 1]
   
H45 = [sin(t5) cos(t5) 0 a5*sin(t5);....
       -cos(t5)  sin(t5) 0 -a5*cos(t5);...
       0           0    1   0;...
       0           0    0    1]
   
H05 = H01*H12*H23*H34*H45

%%
H05 = simplify(H01*H12*H23*H34*H45)
Px = simplify(H05(1,4))
Py = simplify(H05(2,4))
Pz = simplify(H05(3,4))




 