function [theta,J_history]=grad_descent(x,y,alpha,iter,theta)
m=length(y);
n=size(x,2);
J_history=zeros(iter,1);

for i=1:iter
dJ=(x*theta-y)/m;
for j=1:n
theta(j)=theta(j)-alpha*(dJ'*x(:,j));
end
J_history(i)=costfunc(x,y,theta);
end