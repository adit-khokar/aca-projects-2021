function [J,grad]=log_costfunc(x,y,theta,lambda)
m=length(y);
grad=zeros(size(theta));
J=0;
a=-(sum(y.*log(sigmoid(x*theta))+(1-y).*(log(1-sigmoid(x*theta)) )  )   )/m;
reg=sum(theta(2:length(theta),:).^2)*lambda/(2*m);
J=a+reg;
grad=x'*(sigmoid(x*theta)-y)/m + lambda*[0;theta(2:length(theta),:)]/m;
end