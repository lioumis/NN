import keras
from keras.layers import Dense
from keras.models import Sequential
import numpy
from numpy import loadtxt
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold

# Φόρτωση δεδομένων εισόδου και εξόδου.
dataset = loadtxt('C:\\Users\\User\\Desktop\\Input.csv', delimiter=',')
dataset2 = loadtxt('C:\\Users\\User\\Desktop\\Output(centered).csv', delimiter=',')

# Χωρισμός σε μεταβλητές εισόδου και εξόδου.
X = dataset[:,:]
y = dataset2[:,:]

# Early stopping
es = keras.callbacks.callbacks.EarlyStopping(monitor='val_loss', min_delta=0, patience=50, verbose=1, mode='auto', baseline=None, restore_best_weights=False)

# 5-Fold
kfold = KFold(n_splits=5, shuffle=True)

# Λίστες με τα σφάλματα κάθε fold
rmseList = []
maeList = []

for i, (train, test) in enumerate(kfold.split(X)):

    model = Sequential()
    model.add(Dense(45, input_dim=943, activation='relu'))  # activity_regularizer=keras.regularizers.l1(0.1) Χρησιμοποιήθηκε για το ερώτημα Α4
    # model.add(Dense(45, activation='relu')) # Χρησιμοποιήθηκαν για το ερώτημα Α5
    # model.add(Dense(70, activation='relu'))
    model.add(Dense(1682, activation='linear'))


    def rmse(y_true, y_pred): # Ορισμός ρίζας μεσου τετραγωνικού σφάλματος
        return keras.backend.sqrt(keras.backend.mean(keras.backend.square(y_pred - y_true)))

    model.compile(loss='mean_squared_error', optimizer=keras.optimizers.SGD(learning_rate=0.1, momentum=0.6, nesterov=False), metrics=[rmse, 'mean_absolute_error'])

    history = model.fit(X[train], y[train], epochs=1000, batch_size=20, validation_data=(X[test], y[test]), callbacks=[es])

    # Αξιολόγηση του μοντέλου
    scores = model.evaluate(X[test], y[test], verbose=0)
    rmseList.append(scores[1])
    maeList.append(scores[2])

    print("Fold :", i, " RMSE:", scores[1])
    print("Fold :", i, " MAE:", scores[2])

    plt.plot(history.history['rmse'])
    plt.title('Model loss')
    plt.ylabel('RMSE')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper left')
    plt.show()

# Εμφάνιση μετρικών μετά από το 5-fold CV
print("RMSE: ", numpy.mean(rmseList))
print("MAE: ", numpy.mean(maeList))