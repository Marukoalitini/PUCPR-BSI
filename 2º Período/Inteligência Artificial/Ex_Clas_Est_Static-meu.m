%% Database
clear 
clc
close all
%% Preparação dos dados
load("DataSet.mat");
Targets = DataSet(:, end);
Inputs = DataSet(:, 1:end-1);

% Dividir os dados em treinamento (70%) e teste (30%) utilizando hold-out simples
cv = cvpartition(Targets, 'HoldOut', 0.3);
Inp_Train = Inputs(training(cv), :);
Tar_Train = Targets(training(cv));
Inp_Test = Inputs(test(cv), :);
Tar_Test = Targets(test(cv));

%% Modelos de Classificação

% 1. Regressão Logística (LoR)
ML_LoR = fitclinear(Inp_Train, Tar_Train, 'Learner', 'logistic');
Out_Train_LoR = round(predict(ML_LoR, Inp_Train));
Out_Test_LoR = round(predict(ML_LoR, Inp_Test));

% 2. k-Nearest Neighbors (kNN)
ML_kNN = fitcknn(Inp_Train, Tar_Train, 'NumNeighbors', 5);
Out_Train_kNN = predict(ML_kNN, Inp_Train);
Out_Test_kNN = predict(ML_kNN, Inp_Test);

% 3. Naive Bayes (NB)
ML_NB = fitcnb(Inp_Train, Tar_Train);
Out_Train_NB = predict(ML_NB, Inp_Train);
Out_Test_NB = predict(ML_NB, Inp_Test);

% 4. Support Vector Machine (SVM)
ML_SVM = fitcsvm(Inp_Train, Tar_Train);
Out_Train_SVM = predict(ML_SVM, Inp_Train);
Out_Test_SVM = predict(ML_SVM, Inp_Test);

%% Cálculo das Matrizes de Confusão

% Matriz de Confusão para cada modelo nos dados de treinamento
confMatrix_Train_LoR = confusionmat(Tar_Train, Out_Train_LoR);
confMatrix_Train_kNN = confusionmat(Tar_Train, Out_Train_kNN);
confMatrix_Train_NB = confusionmat(Tar_Train, Out_Train_NB);
confMatrix_Train_SVM = confusionmat(Tar_Train, Out_Train_SVM);

% Matriz de Confusão para cada modelo nos dados de teste
confMatrix_Test_LoR = confusionmat(Tar_Test, Out_Test_LoR);
confMatrix_Test_kNN = confusionmat(Tar_Test, Out_Test_kNN);
confMatrix_Test_NB = confusionmat(Tar_Test, Out_Test_NB);
confMatrix_Test_SVM = confusionmat(Tar_Test, Out_Test_SVM);

% Exibir as Matrizes de Confusão para o Conjunto de Treinamento
disp('Matriz de Confusão - Logistic Regression (LoR) - Treinamento:');
disp(confMatrix_Train_LoR);
disp('Matriz de Confusão - k-Nearest Neighbors (kNN) - Treinamento:');
disp(confMatrix_Train_kNN);
disp('Matriz de Confusão - Naive Bayes (NB) - Treinamento:');
disp(confMatrix_Train_NB);
disp('Matriz de Confusão - Support Vector Machine (SVM) - Treinamento:');
disp(confMatrix_Train_SVM);

% Exibir as Matrizes de Confusão para o Conjunto de Teste
disp('Matriz de Confusão - Logistic Regression (LoR) - Teste:');
disp(confMatrix_Test_LoR);
disp('Matriz de Confusão - k-Nearest Neighbors (kNN) - Teste:');
disp(confMatrix_Test_kNN);
disp('Matriz de Confusão - Naive Bayes (NB) - Teste:');
disp(confMatrix_Test_NB);
disp('Matriz de Confusão - Support Vector Machine (SVM) - Teste:');
disp(confMatrix_Test_SVM);

%% Visualizar as Matrizes de Confusão

figure;
% Matrizes de Confusão para Treinamento
subplot(2, 4, 1);
confusionchart(Tar_Train, Out_Train_LoR);
title('Logistic Regression (LoR) - Treinamento');

subplot(2, 4, 2);
confusionchart(Tar_Train, Out_Train_kNN);
title('k-Nearest Neighbors (kNN) - Treinamento');

subplot(2, 4, 3);
confusionchart(Tar_Train, Out_Train_NB);
title('Naive Bayes (NB) - Treinamento');

subplot(2, 4, 4);
confusionchart(Tar_Train, Out_Train_SVM);
title('Support Vector Machine (SVM) - Treinamento');

% Matrizes de Confusão para Teste
subplot(2, 4, 5);
confusionchart(Tar_Test, Out_Test_LoR);
title('Logistic Regression (LoR) - Teste');

subplot(2, 4, 6);
confusionchart(Tar_Test, Out_Test_kNN);
title('k-Nearest Neighbors (kNN) - Teste');

subplot(2, 4, 7);
confusionchart(Tar_Test, Out_Test_NB);
title('Naive Bayes (NB) - Teste');

subplot(2, 4, 8);
confusionchart(Tar_Test, Out_Test_SVM);
title('Support Vector Machine (SVM) - Teste');

%% Cálculo de Precision e Recall

% Função para calcular Precision e Recall a partir da Matriz de Confusão
function [precision, recall] = calcPrecisionRecall(confMatrix)
    TP = confMatrix(1, 1);
    FP = confMatrix(1, 2);
    FN = confMatrix(2, 1);
    TN = confMatrix(2, 2);
    
    precision = TP / (TP + FP);
    recall = TP / (TP + FN);
end

% Calcular Precision e Recall para cada modelo no Conjunto de Treinamento
[precision_Train_LoR, recall_Train_LoR] = calcPrecisionRecall(confMatrix_Train_LoR);
[precision_Train_kNN, recall_Train_kNN] = calcPrecisionRecall(confMatrix_Train_kNN);
[precision_Train_NB, recall_Train_NB] = calcPrecisionRecall(confMatrix_Train_NB);
[precision_Train_SVM, recall_Train_SVM] = calcPrecisionRecall(confMatrix_Train_SVM);

% Calcular Precision e Recall para cada modelo no Conjunto de Teste
[precision_Test_LoR, recall_Test_LoR] = calcPrecisionRecall(confMatrix_Test_LoR);
[precision_Test_kNN, recall_Test_kNN] = calcPrecisionRecall(confMatrix_Test_kNN);
[precision_Test_NB, recall_Test_NB] = calcPrecisionRecall(confMatrix_Test_NB);
[precision_Test_SVM, recall_Test_SVM] = calcPrecisionRecall(confMatrix_Test_SVM);

% Exibir os resultados para o Conjunto de Treinamento
fprintf('\nPrecision e Recall no Conjunto de Treinamento:\n');
fprintf('Logistic Regression (LoR): Precision = %.4f, Recall = %.4f\n', precision_Train_LoR, recall_Train_LoR);
fprintf('k-Nearest Neighbors (kNN): Precision = %.4f, Recall = %.4f\n', precision_Train_kNN, recall_Train_kNN);
fprintf('Naive Bayes (NB): Precision = %.4f, Recall = %.4f\n', precision_Train_NB, recall_Train_NB);
fprintf('Support Vector Machine (SVM): Precision = %.4f, Recall = %.4f\n', precision_Train_SVM, recall_Train_SVM);

% Exibir os resultados para o Conjunto de Teste
fprintf('\nPrecision e Recall no Conjunto de Teste:\n');
fprintf('Logistic Regression (LoR): Precision = %.4f, Recall = %.4f\n', precision_Test_LoR, recall_Test_LoR);
fprintf('k-Nearest Neighbors (kNN): Precision = %.4f, Recall = %.4f\n', precision_Test_kNN, recall_Test_kNN);
fprintf('Naive Bayes (NB): Precision = %.4f, Recall = %.4f\n', precision_Test_NB, recall_Test_NB);
fprintf('Support Vector Machine (SVM): Precision = %.4f, Recall = %.4f\n', precision_Test_SVM, recall_Test_SVM);
