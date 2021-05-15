function g=sigmoid(x)
g=zeros(size(x));
g=1./(exp(-x)+1);
end