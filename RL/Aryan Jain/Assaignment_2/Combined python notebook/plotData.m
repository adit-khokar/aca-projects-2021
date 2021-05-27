% ignore (just for figure)
function plotData(X, y)
figure; hold on;
x1=X(:,1);
x2=X(:,2);
plot(x1(y==1),x2(y==1),'k+','LineWidth', 2, 'MarkerSize', 7);
hold on
plot(x1(y==0),x2(y==0),'ko', 'MarkerFaceColor', 'y','MarkerSize', 7);
hold off;
end