###Behaviour Classification###

df["behaviour"] = 0
df.loc[((df["EPM_total_distance_cm"] <= wt_mice["EPM_total_distance_cm"].mean()) 
       & (df["EPM_velolocity_cm/s"] <= wt_mice['EPM_velolocity_cm/s'].mean())
       & (df["EPM_open_arm_duration_s"] <= wt_mice["EPM_open_arm_duration_s"].mean())), 'behaviour'] = 1

####EPM Behaviour###
       
behaviour = []
for i in rows.iterrows():
    distance = i[1]["EPM_total_distance_cm"]
    velocity = i[1]['EPM_velolocity_cm/s']
    mobility = i[1]['EPM_mobility_s']
    open_arm_freq = i[1]['EPM_open_arm_freq_counts']
    open_arm_duration = i[1]['EPM_open_arm_duration_s']
    closed_arm_freq = i[1]['EPM_closed_arm_freq_counts']
    vertical_activity = i[1]['EPM_vertikal_activity_counts']
    if \
    (distance <= wt_mice['EPM_total_distance_cm'].mean())and \
    (mobility <= wt_mice['EPM_mobility_s'].mean())and \
    (open_arm_freq <= wt_mice['EPM_open_arm_freq_counts'].mean()) and \
    (open_arm_duration <= wt_mice['EPM_open_arm_duration_s'].mean()) and \
    (vertical_activity <= wt_mice['EPM_vertikal_activity_counts'].mean()):
        behaviour.append(1)
    else:
        behaviour.append(0)
df["anxiety"] = behaviour

###OF Behaviour####

behaviour = []
for i in rows.iterrows():
    center_freq = i[1]['OF_center_freq_counts']
    periphery_freq = i[1]['OF_outer_zone_freq_counts']
    distance = i[1]['OF_total_distance_cm']
    vertical_activity = i[1]['OF_vertical_activity']
    mobility = i[1]['OF_mobility_s']
    immobility = i[1]['OF_immobility_s']
    if (distance <= wt_mice['OF_total_distance_cm'].mean())and \
    (center_freq <= wt_mice['OF_center_freq_counts'].mean()) and\
    (mobility <= wt_mice['OF_mobility_s'].mean()) and \
    (immobility >= wt_mice['OF_immobility_s'].mean()) and \
    (vertical_activity <= wt_mice['OF_vertical_activity'].mean()):
        behaviour.append(1)
    else:
        behaviour.append(0)
df["OF_anxiety"] = behaviour


###EPM PREDICTION###
X= df[['EPM_total_distance_cm', 'EPM_velolocity_cm/s', 'EPM_mobility_s',
       'EPM_immobility_s', 'EPM_open_arm_freq_counts',
       'EPM_open_arm_duration_s', 'EPM_closed_arm_freq_counts',
       'EPM_closed_arm_duration_s', 'EPM_center_freq_counts',
       'EPM__center_duration_s', 'EPM_vertikal_activity_counts']]


from sklearn.cluster import KMeans
model = KMeans(n_clusters=2)
model.fit(X)
print(model.labels_)

###TRAIN TEST SPLIT###
from sklearn.model_selection import train_test_split
train_test_split

###PREDICT###
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train,y_train)

print(model.score(X_test, y_test))
