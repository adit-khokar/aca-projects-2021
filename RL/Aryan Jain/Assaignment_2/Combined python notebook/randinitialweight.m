function w =[theta]
w=zeros(size(theta));
lin=size(theta,1);
lout=size(theta,2);
e=sqrt(6)/(sqrt(lin+lout));
w=rand(size(theta))*2*e-e;
end