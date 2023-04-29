import random

import gym
import numpy as np
def state_idx(position,angle,velocity,angularvelocity):
     # if position>=-4.8 and position<-2.4:
     #     if angle>=-4.2 and  angle<-2.115:
     #         return 0
     #     elif angle>=-2.115 and angle<-0.01:
     #         return 1
     #     elif angle>=-0.01 and angle< 0.2095:
     #         return 2
     #     else:
     #         return 3
     # elif position>=-2.4 and position<0:
     #     if angle>=-4.2 and  angle<-2.115:
     #         return 4
     #     elif angle>=-2.115 and angle<-0.01:
     #         return 5
     #     elif angle>=-0.01 and angle< 0.2095:
     #         return 6
     #     else:
     #         return 7
     # elif position>=0 and position<2.4:
     #     if angle>=-4.2 and  angle<-2.115:
     #         return 8
     #     elif angle>=-2.115 and angle<-0.01:
     #         return 9
     #     elif angle>=-0.01 and angle< 0.2095:
     #         return 10
     #     else:
     #         return 11
     # else:
     #     if angle >= -4.2 and angle < -2.115:
     #         return 12
     #     elif angle >= -2.115 and angle < -0.01:
     #         return 13
     #     elif angle >= -0.01 and angle < 0.2095:
     #         return 14
     #     else:
     #         return 15
     if position>2.4 or position<-2.4 or angle>0.2095 or angle<-0.2095:
         return 0
     elif position<=2.4 and position>1.2:
         if angle<=0.2095 and angle>0.10475:
             if velocity<=2 and velocity>1:
                  if angularvelocity<=3 and angularvelocity>1.5:
                      return 1
                  elif angularvelocity<=1.5 and angularvelocity>0:
                      return 2
                  elif angularvelocity<=0 and angularvelocity>-1.5:
                      return 3
                  else:
                      return 4
             elif velocity<=1 and velocity>0:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 5
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 6
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 7
                 else:
                     return 8
             elif velocity<=0 and velocity>-1:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 9
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 10
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 11
                 else:
                     return 12
             else:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 13
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 14
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 15
                 else:
                     return 16
         elif angle <=0.10475 and angle>0:
             if velocity <= 2 and velocity > 1:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 17
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 18
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 19
                 else:
                     return 20
             elif velocity <= 1 and velocity > 0:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 21
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 22
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 23
                 else:
                     return 24
             elif velocity <= 0 and velocity > -1:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 25
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 26
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 27
                 else:
                     return 28
             else:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 29
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 30
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 31
                 else:
                     return 32
         elif angle<=0 and  angle>-0.10475:
             if velocity <= 2 and velocity > 1:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 33
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 34
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 35
                 else:
                     return 36
             elif velocity <= 1 and velocity > 0:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 37
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 38
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 39
                 else:
                     return 40
             elif velocity <= 0 and velocity > -1:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 41
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 42
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 43
                 else:
                     return 44
             else:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 45
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 46
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 47
                 else:
                     return 48
         else:
             if velocity <= 2 and velocity > 1:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 49
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 50
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 51
                 else:
                     return 52
             elif velocity <= 1 and velocity > 0:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 53
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 54
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 55
                 else:
                     return 56
             elif velocity <= 0 and velocity > -1:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 57
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 58
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 59
                 else:
                     return 60
             else:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 61
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 62
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 63
                 else:
                     return 64
     elif position <= 1.2 and position > 0:
         if angle <= 0.2095 and angle > 0.10475:
             if velocity<=2 and velocity>1:
                  if angularvelocity<=3 and angularvelocity>1.5:
                      return 65
                  elif angularvelocity<=1.5 and angularvelocity>0:
                      return 66
                  elif angularvelocity<=0 and angularvelocity>-1.5:
                      return 67
                  else:
                      return 68
             elif velocity<=1 and velocity>0:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 69
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 70
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 71
                 else:
                     return 72
             elif velocity<=0 and velocity>-1:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 73
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 74
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 75
                 else:
                     return 76
             else:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 77
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 78
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 79
                 else:
                     return 80
         elif angle <= 0.10475 and angle > 0:
             if velocity <= 2 and velocity > 1:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 81
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 82
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 83
                 else:
                     return 84
             elif velocity <= 1 and velocity > 0:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 85
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 86
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 87
                 else:
                     return 88
             elif velocity <= 0 and velocity > -1:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 89
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 90
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 91
                 else:
                     return 92
             else:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 93
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 94
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 95
                 else:
                     return 96
         elif angle <= 0 and angle > -0.10475:
             if velocity <= 2 and velocity > 1:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 97
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 98
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 99
                 else:
                     return 100
             elif velocity <= 1 and velocity > 0:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 101
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 102
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 103
                 else:
                     return 104
             elif velocity <= 0 and velocity > -1:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 105
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 106
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 107
                 else:
                     return 108
             else:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 109
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 110
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 111
                 else:
                     return 112
         else:
             if velocity <= 2 and velocity > 1:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 113
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 114
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 115
                 else:
                     return 116
             elif velocity <= 1 and velocity > 0:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 117
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 118
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 119
                 else:
                     return 120
             elif velocity <= 0 and velocity > -1:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 121
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 122
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 123
                 else:
                     return 124
             else:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 125
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 126
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 127
                 else:
                     return 128
     elif position <= 0 and position > -1.2:
         if angle <= 0.2095 and angle > 0.10475:
             if velocity <= 2 and velocity > 1:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 129
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 130
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 131
                 else:
                     return 132
             elif velocity <= 1 and velocity > 0:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 133
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 134
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 135
                 else:
                     return 136
             elif velocity <= 0 and velocity > -1:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 137
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 138
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 139
                 else:
                     return 140
             else:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 141
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 142
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 143
                 else:
                     return 144
         elif angle <= 0.10475 and angle > 0:
             if velocity <= 2 and velocity > 1:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 145
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 146
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 147
                 else:
                     return 148
             elif velocity <= 1 and velocity > 0:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 149
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 150
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 151
                 else:
                     return 152
             elif velocity <= 0 and velocity > -1:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 153
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 154
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 155
                 else:
                     return 156
             else:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 157
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 158
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 159
                 else:
                     return 160
         elif angle <= 0 and angle > -0.10475:
             if velocity <= 2 and velocity > 1:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 161
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 162
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 163
                 else:
                     return 164
             elif velocity <= 1 and velocity > 0:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 165
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 166
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 167
                 else:
                     return 168
             elif velocity <= 0 and velocity > -1:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 169
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 170
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 171
                 else:
                     return 172
             else:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 173
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 174
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 175
                 else:
                     return 176
         else:
             if velocity <= 2 and velocity > 1:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 177
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 178
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 179
                 else:
                     return 180
             elif velocity <= 1 and velocity > 0:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 181
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 182
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 183
                 else:
                     return 185
             elif velocity <= 0 and velocity > -1:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 186
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 187
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 188
                 else:
                     return 189
             else:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 190
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 191
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 192
                 else:
                     return 193
     else:
         if angle <= 0.2095 and angle > 0.10475:
             if velocity <= 2 and velocity > 1:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 194
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 195
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 196
                 else:
                     return 197
             elif velocity <= 1 and velocity > 0:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 198
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 199
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 200
                 else:
                     return 201
             elif velocity <= 0 and velocity > -1:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 202
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 203
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 204
                 else:
                     return 205
             else:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 206
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 207
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 208
                 else:
                     return 209
         elif angle <= 0.10475 and angle > 0:
             if velocity <= 2 and velocity > 1:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 210
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 211
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 212
                 else:
                     return 213
             elif velocity <= 1 and velocity > 0:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 214
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 215
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 216
                 else:
                     return 217
             elif velocity <= 0 and velocity > -1:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 218
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 219
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 220
                 else:
                     return 221
             else:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 222
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 223
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 224
                 else:
                     return 225
         elif angle <= 0 and angle > -0.10475:
             if velocity<=2 and velocity>1:
                  if angularvelocity<=3 and angularvelocity>1.5:
                      return 226
                  elif angularvelocity<=1.5 and angularvelocity>0:
                      return 227
                  elif angularvelocity<=0 and angularvelocity>-1.5:
                      return 228
                  else:
                      return 229
             elif velocity<=1 and velocity>0:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 230
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 231
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 232
                 else:
                     return 233
             elif velocity<=0 and velocity>-1:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 234
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 235
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 236
                 else:
                     return 237
             else:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 238
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 239
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 240
                 else:
                     return 241
         else:
             if velocity <= 2 and velocity > 1:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 242
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 243
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 244
                 else:
                     return 245
             elif velocity <= 1 and velocity > 0:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 246
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 247
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 248
                 else:
                     return 249
             elif velocity <= 0 and velocity > -1:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 250
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 251
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 252
                 else:
                     return 253
             else:
                 if angularvelocity <= 3 and angularvelocity > 1.5:
                     return 254
                 elif angularvelocity <= 1.5 and angularvelocity > 0:
                     return 255
                 elif angularvelocity <= 0 and angularvelocity > -1.5:
                     return 256
                 else:
                     return 257


if __name__ == '__main__':

 env=gym.make('CartPole-v1')
 qtable=np.random.rand(258,2)
 qtable[0][0]=0
 qtable[0][1]=0
 episode=1
 epsilone=0.05
#rewards=[]
#print(qtable)
 for _ in range(500):
    state,info = env.reset()
    #print(state[0],state[2])
    run=0
    totalreward=0
    while(True):
      action=-1

      st_idx = state_idx(state[0], state[2],state[1],state[3])

      #print(state[0],state[2],st_idx)
      if np.random.rand()<epsilone:
         action=random.randrange(0,2,1)
      else:
        action=np.argmax(qtable[st_idx])
      #print(action)

      state_next, reward, terminated, truncated, info = env.step(action)
      totalreward+=reward
      state_next_idx=state_idx(state_next[0],state_next[2],state_next[1],state_next[3])
      #print(st_idx)
      run += 1
      if  terminated:
          qtable[st_idx][action] = qtable[st_idx][action] + 0.1 * (reward- qtable[st_idx][action])
          #print(state_next[0],state_next[2])
          print('Episode',episode,':')
          #print()
          #print('Qtable:')
          #print()
 #         print('left','right')
  #        print(qtable)
          print()
         # print('Runs',run)
          print('Reward:',totalreward)
          print('.........')
          break


      #print(np.max(qtable[state_next_idx]))
      qtable[st_idx][action]=qtable[st_idx][action]+0.1*(reward+np.max(qtable[state_next_idx])-qtable[st_idx][action])
      state=state_next
      #print(state_next[1],state_next[3])

      #print(state_next,reward)

    episode+=1

 env.close()


