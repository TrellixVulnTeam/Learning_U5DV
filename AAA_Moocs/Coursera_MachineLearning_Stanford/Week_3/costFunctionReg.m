function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
h = sigmoid(X * theta);
J_unreg = (sum(-y' * log(h) - sum((1-y)' * log(1-h))) * 1/m);
theta(1) = 0;
J = J_unreg + sum(theta .^2) * (lambda/(2*m));

unreg_grad = ((X' * (h-y))* (1/m)) ;
theta(1) = 0; 
grad = unreg_grad + theta * lambda/m;

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta






% =============================================================

end
