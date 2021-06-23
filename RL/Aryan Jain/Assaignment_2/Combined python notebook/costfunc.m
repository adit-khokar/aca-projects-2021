function J=costfunc(x,y,theta)
m=length(y);
h=x*theta;
dif=(h-y).^2;
s=sum(dif);
J=s/(2*m);
end