syms t1 t2 t3 t4 t5 Px Py Pz

% t1 = (0)*pi/180
% t2 = (120)*pi/180
% t3 = (270)*pi/180
% t4 = (0)*pi/180
% t5 = (270)*pi/180


VH05 = [ 1     0     0    36;
    0     0    -1     0;
    0     1     0    10;
    0     0     0     1]

H05 =[  sin(t5)*(sin(t1)*sin(t4) - cos(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2))) - cos(t5)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3)), cos(t5)*(sin(t1)*sin(t4) - cos(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2))) + sin(t5)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3)), cos(t4)*sin(t1) + sin(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2)), 13*cos(t1)*cos(t2) + 10*sin(t5)*(sin(t1)*sin(t4) - cos(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2))) - 10*cos(t5)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3)) - 13*cos(t1)*sin(t2)*sin(t3) + 13*cos(t1)*cos(t2)*cos(t3);...
    - sin(t5)*(cos(t1)*sin(t4) + cos(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2))) - cos(t5)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1)), sin(t5)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1)) - cos(t5)*(cos(t1)*sin(t4) + cos(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2))), sin(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2)) - cos(t1)*cos(t4), 13*cos(t2)*sin(t1) - 10*sin(t5)*(cos(t1)*sin(t4) + cos(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2))) - 10*cos(t5)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1)) - 13*sin(t1)*sin(t2)*sin(t3) + 13*cos(t2)*cos(t3)*sin(t1);...
    sin(t2 + t3)*cos(t5) + cos(t2 + t3)*cos(t4)*sin(t5),                                                                                                   cos(t2 + t3)*cos(t4)*cos(t5) - sin(t2 + t3)*sin(t5),                                                         -cos(t2 + t3)*sin(t4),                                                                                                                    13*sin(t2 + t3) + 13*sin(t2) - 5*sin(t4 - t5)*cos(t2 + t3) + 5*cos(t2 + t3)*sin(t4 + t5) + 10*sin(t2 + t3)*cos(t5) + 10;...
    0,                                                                                                                                                     0,                                                                             0,                                                                                                                                                                                                                                          1];
 



[T1 T2 T3 T4 T5] = solve(H05==VH05,t1,t2,t3,t4,t5);
T1 = real((T1)*180/pi)
T2 = real((T2)*180/pi)
T3 = real((T3)*180/pi)
T4 = real((T4)*180/pi)
T5 = real((T5)*180/pi)


%%


% 
% Px = 13*cos(t1)*cos(t2) + 13*sin(t5)*(sin(t1)*sin(t4) - cos(t4)*(cos(t1)*cos(t2)*sin(t3) + cos(t1)*cos(t3)*sin(t2))) - 13*cos(t5)*(cos(t1)*sin(t2)*sin(t3) - cos(t1)*cos(t2)*cos(t3)) - 13*cos(t1)*sin(t2)*sin(t3) + 13*cos(t1)*cos(t2)*cos(t3);
% Py = 13*cos(t2)*sin(t1) - 13*sin(t5)*(cos(t1)*sin(t4) + cos(t4)*(cos(t2)*sin(t1)*sin(t3) + cos(t3)*sin(t1)*sin(t2))) - 13*cos(t5)*(sin(t1)*sin(t2)*sin(t3) - cos(t2)*cos(t3)*sin(t1)) - 13*sin(t1)*sin(t2)*sin(t3) + 13*cos(t2)*cos(t3)*sin(t1);
% Pz = 13*sin(t2 + t3) + 13*sin(t2) - (13*sin(t4 - t5)*cos(t2 + t3))/2 + (13*cos(t2 + t3)*sin(t4 + t5))/2 + 13*sin(t2 + t3)*cos(t5) + 10;


T1 = simplfy(T1)
T2 = simplfy(T2)
T3 = simplfy(T3)
T4 = simplfy(T4)
T5 = simplfy(T5)

% T1 = real(simplfy(T1))*(180/pi)
% T2 = real(simplfy(T2))*(180/pi)
% T3 = real(simplfy(T3))*(180/pi)
% T4 = real(simplfy(T4))*(180/pi)
% T5 = real(simplfy(T5))*(180/pi)