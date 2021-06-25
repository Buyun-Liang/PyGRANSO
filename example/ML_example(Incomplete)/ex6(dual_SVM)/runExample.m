function soln = runExample()
%   runExample: (examples/ex5)
%       Run GRANSO on a 2-variable nonsmooth Rosenbrock objective function,
%       subject to simple bound constraints, with GRANSO's default
%       parameters.
%    
%       Read this source code.
%   
%       This tutorial example shows:
%
%           - how to call GRANSO using objective and constraint functions
%             defined in .m files 
%       
%           - how to set GRANSO's inputs when there aren't any 
%             equality constraint functions (which also applies when there
%             aren't any inequality constraints)
%
%   USAGE:
%       soln = runExample();
% 
%   INPUT: [none]
%   
%   OUTPUT:
%       soln        GRANSO's output struct
%
%   See also objectiveFunction, inequalityConstraint. 

%% read csv
data = readtable('breast-cancer-wisconsin.csv');
[N,p] = size(data);
p = p - 2; % delete index and y

%% specify input variables 
% key: input variables
var = {'alpha'};
% value: dimension. e.g., 3 by 2 => [3,2]
dim = { [N,1] };
var_dim_map =  containers.Map(var, dim);

% calculate total number of scalar variables
nvar = 0;
for idx = 1:length(dim)
    curDim = dim(idx);
    nvar = nvar + curDim{1,1}(1)*curDim{1,1}(2);
end

% regularization parameter
parameters.C = 1;
parameters.data = data;

 
data.Var7 = str2double (data.Var7); 

r = data(:,p+2); % label
x = data(:,2:p+1); % input

r = r{:,:};

r(r == 2) = 0;
r(r == 4) = 1;

x = x{:,:};
x(isnan(x)) = 1;

% parameter
% parameters.H = H;
parameters.label_r = r;
parameters.data_x = x;
parameters.N = N;

opts.maxit = 10;

opts.quadprog_opts.QPsolver = 'qpalm';
% opts.quadprog_opts.QPsolver = 'quadprog';

%% call mat2vec to enable GRANSO using matrix input
tic
combined_fn = @(x) mat2vec(x,var_dim_map,nvar,parameters);
soln = granso(nvar,combined_fn,opts);
toc

end