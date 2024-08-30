%% Database

load("DataSet.mat");
Targets=DataSet(:,end);
Inputs=DataSet(:,1:end-1);

% Visualización rápida de los datos
disp('Inputs:');
disp(Inputs(1:5, :)); % Mostrar las primeras 5 filas de inputs
disp('Targets:');
disp(Targets(1:5)); % Mostrar las primeras 5 filas de targets

%%

% Contar el número de instancias y características
Instances = size(Inputs, 1);
Features = size(Inputs, 2);

% Mostrar la información de instancias y características
fprintf('Number of Instances: %d\n', Instances);
fprintf('Number of Features: %d\n', Features);

%%

% Calcular el balanceo de las clases
classLabels = unique(Targets);
classCounts = histc(Targets, classLabels);

% Mostrar el balanceo de las clases
for i = 1:length(classLabels)
    fprintf('Class %d: %d instances\n', classLabels(i), classCounts(i));
end

%%

% Verificar datos faltantes (NaN) en el conjunto de datos
numMissing = sum(isnan(Inputs));

% Mostrar el número de valores faltantes por característica
disp('Número de valores faltantes (NaN) por característica:');
for i = 1:Features
    fprintf('Feature %d: %d valores faltantes\n', i, numMissing(i));
end

% Verificar si hay alguna fila completa con valores NaN
rowsWithNaN = any(isnan(Inputs), 2);
numRowsWithNaN = sum(rowsWithNaN);

% Mostrar el número de filas con valores NaN
fprintf('Número de filas con valores NaN: %d\n', numRowsWithNaN);

%%

% Calcular la matriz de correlación de Spearman entre las características
correlationMatrix = corr(Inputs, 'Type', 'Spearman');

% Mostrar la matriz de correlación
disp('Spearman Correlation Matrix:');
disp(correlationMatrix);

% Crear un mapa de calor para visualizar la matriz de correlación
figure;
heatmap(correlationMatrix, 'Colormap', jet, 'ColorbarVisible', 'on');
title('Spearman Correlation Matrix');
xlabel('Features');
ylabel('Features');


%%

% Crear boxplots por clase para cada característica
numFeatures = size(Inputs, 2);

% Crear una figura para los boxplots
figure;
for i = 1:numFeatures
    subplot(2, 5, i); % Organiza subfiguras en una cuadrícula
    boxplot(Inputs(:, i), Targets, 'Labels', {'Clase 1', 'Clase 2'});
    title(['Feature Boxplot', num2str(i)]);
    xlabel('Class');
    ylabel(['Feature ', num2str(i)]);
end
sgtitle('Comparison Feature x Class');

%%

% Calcular valores máximos, mínimos, medios y desviación estándar para cada característica
maxValues = max(Inputs);
minValues = min(Inputs);
meanValues = mean(Inputs);
stdValues = std(Inputs);

% Mostrar los valores calculados
disp('Valores máximos, mínimos, medios y desviación estándar para cada característica:');
for i = 1:numFeatures
    fprintf('Feature %d: Máximo = %.4f, Mínimo = %.4f, Media = %.4f, Desviación estándar = %.4f\n', ...
        i, maxValues(i), minValues(i), meanValues(i), stdValues(i));
end

%% 
% Crear histogramas para cada característica
figure;
for i = 1:numFeatures
    subplot(2, 5, i); % Organiza subfiguras en una cuadrícula
    histogram(Inputs(:, i));
    title(['Histograma de Feature ', num2str(i)]);
    xlabel(['Feature ', num2str(i)]);
    ylabel('Frecuencia');
end
sgtitle('Distribución de cada característica');

%%
% Identificación de outliers utilizando el método de Tukey (1.5 IQR)
outliers = zeros(size(Inputs));
for i = 1:numFeatures
    Q1 = quantile(Inputs(:, i), 0.25);
    Q3 = quantile(Inputs(:, i), 0.75);
    IQR = Q3 - Q1;
    outlierIndices = (Inputs(:, i) < Q1 - 1.5 * IQR) | (Inputs(:, i) > Q3 + 1.5 * IQR);
    outliers(:, i) = outlierIndices;
end

% Mostrar el número de outliers por característica
disp('Número de outliers por característica:');
for i = 1:numFeatures
    fprintf('Feature %d: %d outliers\n', i, sum(outliers(:, i)));
end

%%

% Dividir los datos en entrenamiento (70%) y prueba (30%) utilizando hold-out simple
cv = cvpartition(Targets, 'HoldOut', 0.3);

% Crear conjuntos de entrenamiento y prueba
Inp_Train = Inputs(training(cv), :);
Tar_Train = Targets(training(cv));
Inp_Test = Inputs(test(cv), :);
Tar_Test = Targets(test(cv));

% Evaluar el balanceo de las clases en el conjunto de entrenamiento
trainClassLabels = unique(Tar_Train);
trainClassCounts = histc(Tar_Train, trainClassLabels);

disp('Balanceo de clases en el conjunto de entrenamiento:');
for i = 1:length(trainClassLabels)
    fprintf('Clase %d: %d instancias\n', trainClassLabels(i), trainClassCounts(i));
end

% Evaluar el balanceo de las clases en el conjunto de prueba
testClassLabels = unique(Tar_Test);
testClassCounts = histc(Tar_Test, testClassLabels);

disp('Balanceo de clases en el conjunto de prueba:');
for i = 1:length(testClassLabels)
    fprintf('Clase %d: %d instancias\n', testClassLabels(i), testClassCounts(i));
end


%%
% Entrenar un modelo de regresión logística con los datos de entrenamiento
ML_LoR = fitclinear(Inp_Train, Tar_Train, 'Learner','logistic');

%% Predecir las clases para los datos de entrenamiento
Out_Train = round(predict(ML_LoR, Inp_Train));

% Predecir las clases para los datos de prueba
Out_Test = round(predict(ML_LoR, Inp_Test));

% Calcular la matriz de confusión para los datos de entrenamiento
trainConfMatrix = confusionmat(Tar_Train, Out_Train);

% Calcular la matriz de confusión para los datos de prueba
testConfMatrix = confusionmat(Tar_Test, Out_Test);

% Mostrar la matriz de confusión para los datos de entrenamiento
disp('Matriz de Confusión para los Datos de Entrenamiento:');
disp(trainConfMatrix);

% Mostrar la matriz de confusión para los datos de prueba
disp('Matriz de Confusión para los Datos de Prueba:');
disp(testConfMatrix);

% Visualización de la matriz de confusión para los datos de entrenamiento
figure;
confusionchart(Tar_Train, Out_Train);
title('Matriz de Confusión (Entrenamiento)');

% Visualización de la matriz de confusión para los datos de prueba
figure;
confusionchart(Tar_Test, Out_Test);
title('Matriz de Confusión (Prueba)');

%%

% Calcular la matriz de confusión para los datos de entrenamiento
trainConfMatrix = confusionmat(Tar_Train, Out_Train);

% Calcular la matriz de confusión para los datos de prueba
testConfMatrix = confusionmat(Tar_Test, Out_Test);

% Calcular KPIs para los datos de prueba
TP = testConfMatrix(1,1);
FP = testConfMatrix(1,2);
FN = testConfMatrix(2,1);
TN = testConfMatrix(2,2);

accuracy = (TP + TN) / (TP + TN + FP + FN);
% recall = TP / (TP + FN); % Positive class
 recall = TN / (TN + FP); % Negative class
% precision = TP / (TP + FP); % Positive class
 precision = TN / (TN + FN); %Negative class;

f1_score = 2 * (precision * recall) / (precision + recall);
misclassification_ratio = (FP + FN) / (TP + TN + FP + FN);



% Mostrar los KPIs
fprintf('****************\n')
fprintf('Accuracy: %.4f\n', accuracy);
fprintf('Misclassification: %.4f\n', misclassification_ratio);
fprintf('Recall: %.4f\n', recall);
fprintf('F1 Score: %.4f\n', f1_score);

%%

% Configurar k-fold cross-validation con 5 pliegues
k = 5;
cv = cvpartition(Tar_Train, 'KFold', k);

% Inicializar arrays para almacenar los KPIs
accuracyArray = zeros(k, 1);
recallArray = zeros(k, 1);
precisionArray = zeros(k, 1);
f1Array = zeros(k, 1);
misclassificationArray = zeros(k, 1);

% Realizar k-fold cross-validation
for i = 1:k
    % Dividir los datos en conjuntos de entrenamiento y validación
    trainIdx = training(cv, i);
    testIdx = test(cv, i);
    Inp_Train_k = Inp_Train(trainIdx, :);
    Tar_Train_k = Tar_Train(trainIdx);
    Inp_Test_k = Inp_Train(testIdx, :);
    Tar_Test_k = Tar_Train(testIdx);
    
    % Entrenar el modelo
    % model = fitclinear(Inp_Train_k, Tar_Train_k, 'Learner', 'logistic');
    model = fitcnb(Inp_Train_k, Tar_Train_k);

    % Realizar predicciones
    predictions = predict(model, Inp_Test_k);
    
    % Calcular la matriz de confusión
    confMatrix = confusionmat(Tar_Test_k, predictions);
    TP = confMatrix(1, 1);
    FP = confMatrix(1, 2);
    FN = confMatrix(2, 1);
    TN = confMatrix(2, 2);
    
    % Calcular los KPIs
    accuracyArray(i) = (TP + TN) / (TP + TN + FP + FN);
    recallArray(i) = TP / (TP + FN);
    precisionArray(i) = TP / (TP + FP);
    f1Array(i) = 2 * (precisionArray(i) * recallArray(i)) / (precisionArray(i) + recallArray(i));
    misclassificationArray(i) = (FP + FN) / (TP + TN + FP + FN);
end

% Calcular los valores medios y desviaciones estándar de los KPIs
meanAccuracy = mean(accuracyArray);
stdAccuracy = std(accuracyArray);

meanRecall = mean(recallArray);
stdRecall = std(recallArray);

meanPrecision = mean(precisionArray);
stdPrecision = std(precisionArray);

meanF1 = mean(f1Array);
stdF1 = std(f1Array);

meanMisclassification = mean(misclassificationArray);
stdMisclassification = std(misclassificationArray);

% Mostrar los resultados
fprintf('K-Fold Cross-Validation Results (k = %d):\n', k);
fprintf('Accuracy: Mean = %.4f, Std = %.4f\n', meanAccuracy, stdAccuracy);
fprintf('Misclassification: Mean = %.4f, Std = %.4f\n', meanMisclassification, stdMisclassification);
fprintf('Recall: Mean = %.4f, Std = %.4f\n', meanRecall, stdRecall);
fprintf('Precision: Mean = %.4f, Std = %.4f\n', meanPrecision, stdPrecision);
fprintf('F1 Score: Mean = %.4f, Std = %.4f\n', meanF1, stdF1);
