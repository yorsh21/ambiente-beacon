import json
import random

sensors = [{"id": 1, "lat": -33.4584, "lng": -70.709},{"id": 2, "lat": -33.4392, "lng": -70.673},{"id": 3, "lat": -33.5276, "lng": -70.569},{"id": 4, "lat": -33.5056, "lng": -70.590},{"id": 5, "lat": -33.3923, "lng": -70.588},{"id": 8, "lat": -33.43, "lng": -70.683},{"id": 10, "lat": -33.5497, "lng": -70.580},{"id": 11, "lat": -33.3814, "lng": -70.68},{"id": 15, "lat": -33.5428, "lng": -70.681},{"id": 16, "lat": -33.6262, "lng": -70.591},{"id": 18, "lat": -33.3763, "lng": -70.548},{"id": 19, "lat": -33.4547, "lng": -70.626},{"id": 20, "lat": -33.437, "lng": -70.545},{"id": 21, "lat": -33.4227, "lng": -70.587},{"id": 22, "lat": -33.5568, "lng": -70.652},{"id": 23, "lat": -33.616, "lng": -70.700},{"id": 24, "lat": -33.3803, "lng": -70.537},{"id": 25, "lat": -33.4919, "lng": -70.768},{"id": 26, "lat": -33.4314, "lng": -70.573},{"id": 27, "lat": -33.5205, "lng": -70.598},{"id": 28, "lat": -33.452, "lng": -70.608},{"id": 29, "lat": -33.4706, "lng": -70.612},{"id": 30, "lat": -33.5554, "lng": -70.584},{"id": 31, "lat": -33.46, "lng": -70.595},{"id": 32, "lat": -33.4895, "lng": -70.598},{"id": 33, "lat": -33.5921, "lng": -70.5555},{"id": 34, "lat": -33.463, "lng": -70.6882},{"id": 35, "lat": -33.5754, "lng": -70.5624},{"id": 36, "lat": -33.5756, "lng": -70.5626},{"id": 37, "lat": -33.4375, "lng": -70.6569},{"id": 38, "lat": -33.441, "lng": -70.6226},{"id": 39, "lat": -33.4425, "lng": -70.5766},{"id": 41, "lat": -33.4896, "lng": -70.6712},{"id": 43, "lat": -33.5277, "lng": -70.7646},{"id": 45, "lat": -33.4678, "lng": -70.5361},{"id": 46, "lat": -33.5448, "lng": -70.582},{"id": 47, "lat": -33.3925, "lng": -70.5039},{"id": 48, "lat": -33.4496, "lng": -70.6464},{"id": 49, "lat": -33.4869, "lng": -70.7668},{"id": 50, "lat": -33.4871, "lng": -70.7384},{"id": 51, "lat": -33.4652, "lng": -70.7523},{"id": 52, "lat": -33.4564, "lng": -70.6583},{"id": 53, "lat": -33.4443, "lng": -70.6309},{"id": 54, "lat": -33.4337, "lng": -70.6647},{"id": 55, "lat": -33.4382, "lng": -70.6564},{"id": 56, "lat": -33.5268, "lng": -70.6534},{"id": 57, "lat": -33.5322, "lng": -70.6562},{"id": 58, "lat": -33.45, "lng": -70.6667},{"id": 59, "lat": -33.4095, "lng": -70.6614},{"id": 60, "lat": -33.4297, "lng": -70.656},{"id": 61, "lat": -33.4701, "lng": -70.6694},{"id": 62, "lat": -33.5308, "lng": -70.791},{"id": 63, "lat": -33.5617, "lng": -70.5876},{"id": 64, "lat": -33.0311, "lng": -71.5365},{"id": 65, "lat": -33.0311, "lng": -71.5365},{"id": 66, "lat": -33.0284, "lng": -71.5749},{"id": 67, "lat": -33.0278, "lng": -71.5847},{"id": 68, "lat": -33.0404, "lng": -71.3511},{"id": 69, "lat": -33.0202, "lng": -71.5415},{"id": 70, "lat": -33.0164, "lng": -71.554},{"id": 71, "lat": -33.4365, "lng": -70.6199},{"id": 72, "lat": -33.1181, "lng": -71.581},{"id": 73, "lat": -33.12, "lng": -71.5822},{"id": 74, "lat": -33.0453, "lng": -71.6165},{"id": 75, "lat": -33.053, "lng": -71.6283},{"id": 76, "lat": -34.1356, "lng": -70.7368},{"id": 77, "lat": -33.4375, "lng": -70.6434},{"id": 78, "lat": -33.4407, "lng": -70.6419},{"id": 79, "lat": -33.4516, "lng": -70.6662},{"id": 81, "lat": -45.5825, "lng": -72.0412},{"id": 82, "lat": -45.573, "lng": -72.0325},{"id": 83, "lat": -45.5788, "lng": -72.0573},{"id": 84, "lat": -45.5837, "lng": -72.0577},{"id": 86, "lat": -33.4344, "lng": -70.6591},{"id": 87, "lat": -33.4256, "lng": -70.6863},{"id": 88, "lat": -33.4102, "lng": -70.6929},{"id": 89, "lat": -33.5649, "lng": -70.7985},{"id": 90, "lat": -33.5275, "lng": -70.6368},{"id": 91, "lat": -33.3735, "lng": -70.6898},{"id": 92, "lat": -33.554, "lng": -70.5835},{"id": 93, "lat": -33.4658, "lng": -70.7031},{"id": 94, "lat": -33.4292, "lng": -70.658},{"id": 95, "lat": -33.5688, "lng": -70.7762},{"id": 96, "lat": -33.4721, "lng": -70.7329},{"id": 97, "lat": -33.4579, "lng": -70.6432},{"id": 98, "lat": -33.4417, "lng": -70.66},{"id": 99, "lat": -33.4358, "lng": -70.6557},{"id": 100, "lat": -33.4753, "lng": -70.7205},{"id": 101, "lat": -33.4625, "lng": -70.6682},{"id": 102, "lat": -45.5759, "lng": -72.054},{"id": 103, "lat": -33.4472, "lng": -70.6849},{"id": 104, "lat": -33.5215, "lng": -70.5637},{"id": 105, "lat": -33.4772, "lng": -70.5202},{"id": 106, "lat": -33.45, "lng": -70.6667},{"id": 107, "lat": -33.5057, "lng": -70.5475},{"id": 108, "lat": -33.4815, "lng": -70.6085},{"id": 109, "lat": -33.494, "lng": -70.5952},{"id": 110, "lat": -33.4459, "lng": -70.6024},{"id": 111, "lat": -33.5398, "lng": -70.5514},{"id": 112, "lat": -33.5909, "lng": -70.5992},{"id": 113, "lat": -33.5923, "lng": -70.5855},{"id": 114, "lat": -33.6289, "lng": -70.7041},{"id": 115, "lat": -33.5515, "lng": -70.6647},{"id": 116, "lat": -33.4791, "lng": -70.5949},{"id": 117, "lat": -33.482, "lng": -70.5837},{"id": 118, "lat": -33.4813, "lng": -70.5829},{"id": 119, "lat": -33.4814, "lng": -70.5922},{"id": 120, "lat": -33.431, "lng": -70.5731},{"id": 121, "lat": -33.4283, "lng": -70.564},{"id": 122, "lat": -33.1109, "lng": -71.5628},{"id": 123, "lat": -33.4625, "lng": -70.6682},{"id": 124, "lat": -33.1502, "lng": -71.5663},{"id": 125, "lat": -33.1142, "lng": -71.5545},{"id": 126, "lat": -33.0585, "lng": -71.5831},{"id": 127, "lat": -33.4293, "lng": -70.6285},{"id": 128, "lat": -33.5625, "lng": -70.6215},{"id": 130, "lat": -33.4549, "lng": -70.5773},{"id": 131, "lat": -33.4629, "lng": -70.6249},{"id": 132, "lat": -33.4568, "lng": -70.5981},{"id": 133, "lat": -33.4401, "lng": -70.6141},{"id": 134, "lat": -33.4716, "lng": -70.7042},{"id": 135, "lat": -45.5728, "lng": -72.0511},{"id": 136, "lat": -33.3772, "lng": -70.6341},{"id": 137, "lat": -33.4166, "lng": -70.6942},{"id": 138, "lat": -33.4971, "lng": -70.7295},{"id": 139, "lat": -33.8043, "lng": -70.7283},{"id": 140, "lat": -33.4166, "lng": -70.5694},{"id": 141, "lat": -33.3744, "lng": -70.5423},{"id": 142, "lat": -33.4203, "lng": -70.5816},{"id": 143, "lat": -33.4458, "lng": -70.6381},{"id": 144, "lat": -33.4355, "lng": -70.6541},{"id": 145, "lat": -33.4416, "lng": -70.5812},{"id": 146, "lat": -33.563, "lng": -70.5553},{"id": 147, "lat": -33.4082, "lng": -70.6417},{"id": 148, "lat": -45.5838, "lng": -72.0572},{"id": 149, "lat": -33.4541, "lng": -70.5917},{"id": 150, "lat": -33.6218, "lng": -70.887},{"id": 151, "lat": -33.6218, "lng": -70.887},{"id": 152, "lat": -45.5872, "lng": -72.0711},{"id": 153, "lat": -33.4033, "lng": -70.5516},{"id": 154, "lat": -33.4412, "lng": -70.581},{"id": 155, "lat": -33.4439, "lng": -70.6352},{"id": 156, "lat": -33.4457, "lng": -70.6397},{"id": 157, "lat": -33.4492, "lng": -70.6558},{"id": 158, "lat": -33.4527, "lng": -70.7454},{"id": 159, "lat": -33.4219, "lng": -70.6059},{"id": 160, "lat": -33.4431, "lng": -70.6764},{"id": 161, "lat": -33.4448, "lng": -70.672},{"id": 162, "lat": -45.5882, "lng": -72.0523},{"id": 163, "lat": -33.4565, "lng": -70.6096},{"id": 164, "lat": -33.3729, "lng": -70.6886},{"id": 165, "lat": -33.5954, "lng": -71.5978},{"id": 166, "lat": -33.5961, "lng": -71.596},{"id": 167, "lat": -33.5961, "lng": -71.596},{"id": 168, "lat": -33.5793, "lng": -71.6107},{"id": 169, "lat": -33.3771, "lng": -71.6872},{"id": 170, "lat": -33.2744, "lng": -71.4823},{"id": 171, "lat": -32.9944, "lng": -71.5231},{"id": 172, "lat": -33.0316, "lng": -71.576},{"id": 173, "lat": -33.0321, "lng": -71.5637},{"id": 174, "lat": -33.4283, "lng": -70.6215},{"id": 175, "lat": -33.119, "lng": -71.5786},{"id": 176, "lat": -33.0081, "lng": -71.5197},{"id": 177, "lat": -33.0444, "lng": -71.4528},{"id": 178, "lat": -33.0592, "lng": -71.4369},{"id": 179, "lat": -33.0455, "lng": -71.4515},{"id": 180, "lat": -33.0578, "lng": -71.4258},{"id": 181, "lat": -33.0542, "lng": -71.4104},{"id": 182, "lat": -33.0546, "lng": -71.4084},{"id": 183, "lat": -33.0081, "lng": -71.5197},{"id": 184, "lat": -32.9494, "lng": -71.5407},{"id": 185, "lat": -33.0345, "lng": -71.5034},{"id": 186, "lat": -32.9744, "lng": -71.5392},{"id": 187, "lat": -32.9626, "lng": -71.5422},{"id": 188, "lat": -33.0461, "lng": -71.6015},{"id": 189, "lat": -33.0617, "lng": -71.5805},{"id": 190, "lat": -33.0442, "lng": -71.6285},{"id": 191, "lat": -33.0442, "lng": -71.6176},{"id": 192, "lat": -33.0422, "lng": -71.3733},{"id": 193, "lat": -33.0436, "lng": -71.6038},{"id": 194, "lat": -33.1233, "lng": -71.5826},{"id": 195, "lat": -33.061, "lng": -71.3731},{"id": 196, "lat": -33.0709, "lng": -71.4346},{"id": 197, "lat": -33.0367, "lng": -71.368},{"id": 198, "lat": -32.9506, "lng": -71.5403},{"id": 199, "lat": -33.0258, "lng": -71.5476},{"id": 200, "lat": -33.0279, "lng": -71.5504},{"id": 201, "lat": -33.029, "lng": -71.5788},{"id": 202, "lat": -33.009, "lng": -71.4852},{"id": 203, "lat": -33.0013, "lng": -71.5189},{"id": 204, "lat": -33.3043, "lng": -70.7417},{"id": 205, "lat": -33.0486, "lng": -71.5602},{"id": 206, "lat": -32.9881, "lng": -71.5254},{"id": 207, "lat": -33.0268, "lng": -71.5523},{"id": 208, "lat": -33.0204, "lng": -71.5113},{"id": 209, "lat": -33.0382, "lng": -71.4785},{"id": 210, "lat": -33.45, "lng": -70.6667},{"id": 211, "lat": -33.045, "lng": -71.5627},{"id": 213, "lat": -33.4083, "lng": -70.5754},{"id": 214, "lat": -23.6616, "lng": -70.4028},{"id": 215, "lat": -23.5752, "lng": -70.3893},{"id": 216, "lat": -23.6801, "lng": -70.4037},{"id": 217, "lat": -23.6773, "lng": -70.401},{"id": 218, "lat": -23.6762, "lng": -70.4026},{"id": 219, "lat": -23.6153, "lng": -70.3817},{"id": 220, "lat": -23.6178, "lng": -70.3871},{"id": 221, "lat": -23.6296, "lng": -70.3904},{"id": 222, "lat": -23.656, "lng": -70.3979},{"id": 223, "lat": -23.6562, "lng": -70.3979},{"id": 224, "lat": -23.6856, "lng": -70.4096},{"id": 225, "lat": -23.6856, "lng": -70.4096},{"id": 226, "lat": -33.4371, "lng": -70.6625},{"id": 227, "lat": -23.5921, "lng": -70.3793},{"id": 228, "lat": -23.5884, "lng": -70.3772},{"id": 229, "lat": -23.58, "lng": -70.3785},{"id": 230, "lat": -23.5766, "lng": -70.3817},{"id": 231, "lat": -23.6509, "lng": -70.3975},{"id": 232, "lat": -23.6317, "lng": -70.3931},{"id": 233, "lat": -23.6752, "lng": -70.4058},{"id": 234, "lat": -23.5779, "lng": -70.3856},{"id": 235, "lat": -23.6491, "lng": -70.4016},{"id": 236, "lat": -23.695, "lng": -70.4198},{"id": 237, "lat": -23.7075, "lng": -70.4267},{"id": 238, "lat": -23.6655, "lng": -70.4029},{"id": 239, "lat": -23.5594, "lng": -70.3913},{"id": 240, "lat": -23.5595, "lng": -70.3915},{"id": 241, "lat": -23.65, "lng": -70.4},{"id": 242, "lat": -23.6779, "lng": -70.4059},{"id": 243, "lat": -23.6394, "lng": -70.3954},{"id": 244, "lat": -23.6878, "lng": -70.4061},{"id": 245, "lat": -38.7277, "lng": -72.6205},{"id": 246, "lat": -38.7156, "lng": -72.6517},{"id": 247, "lat": -38.717, "lng": -72.6079},{"id": 248, "lat": -38.717, "lng": -72.6079},{"id": 249, "lat": -38.7124, "lng": -72.6256},{"id": 250, "lat": -38.7452, "lng": -72.6297},{"id": 251, "lat": -38.7458, "lng": -72.6288},{"id": 252, "lat": -38.7431, "lng": -72.6323},{"id": 253, "lat": -38.7426, "lng": -72.6459},{"id": 254, "lat": -38.74, "lng": -7.644},{"id": 255, "lat": -38.7157, "lng": -72.6567},{"id": 256, "lat": -38.7431, "lng": -72.6323},{"id": 257, "lat": -38.7499, "lng": -72.6413},{"id": 258, "lat": -38.7398, "lng": -72.6434},{"id": 259, "lat": -38.7431, "lng": -72.6323},{"id": 260, "lat": -38.7351, "lng": -72.6408},{"id": 261, "lat": -38.6972, "lng": -72.5356},{"id": 262, "lat": -38.7333, "lng": -72.6},{"id": 263, "lat": -38.7408, "lng": -72.596},{"id": 264, "lat": -38.7248, "lng": -72.6225},{"id": 265, "lat": -38.6997, "lng": -72.5372},{"id": 266, "lat": -38.7337, "lng": -72.6235},{"id": 267, "lat": -38.7415, "lng": -72.5912},{"id": 268, "lat": -33.4108, "lng": -70.5764},{"id": 269, "lat": -33.4357, "lng": -70.6569},{"id": 270, "lat": -45.5869, "lng": -72.0398},{"id": 271, "lat": -33.5117, "lng": -70.5478},{"id": 272, "lat": -38.7355, "lng": -72.6347},{"id": 273, "lat": -38.7355, "lng": -72.6347},{"id": 274, "lat": -38.7576, "lng": -72.6002},{"id": 275, "lat": -38.748, "lng": -72.6429},{"id": 276, "lat": -38.7355, "lng": -72.6347},{"id": 277, "lat": -33.45, "lng": -70.6667},{"id": 278, "lat": -38.7593, "lng": -72.6286},{"id": 279, "lat": -38.744, "lng": -72.5969},{"id": 280, "lat": -38.7327, "lng": -72.6365},{"id": 281, "lat": -38.7314, "lng": -72.5587},{"id": 282, "lat": -38.7593, "lng": -72.6286},{"id": 283, "lat": -38.7575, "lng": -72.6003},{"id": 284, "lat": -38.7243, "lng": -72.6336},{"id": 285, "lat": -33.5535, "lng": -70.5725},{"id": 286, "lat": -33.5536, "lng": -70.5727},{"id": 287, "lat": -33.5536, "lng": -70.5727},{"id": 288, "lat": -33.5532, "lng": -70.5729},{"id": 289, "lat": -33.5332, "lng": -70.5482},{"id": 290, "lat": -33.5532, "lng": -70.5729},{"id": 291, "lat": -38.706, "lng": -72.5468},{"id": 292, "lat": -38.7295, "lng": -72.6194},{"id": 293, "lat": -38.7297, "lng": -72.5669},{"id": 294, "lat": -38.7578, "lng": -72.5946},{"id": 295, "lat": -38.7353, "lng": -72.5968},{"id": 296, "lat": -38.7563, "lng": -72.6594},{"id": 297, "lat": -38.7491, "lng": -72.6442},{"id": 298, "lat": -38.7355, "lng": -72.6347},{"id": 299, "lat": -38.7398, "lng": -72.6494},{"id": 300, "lat": -38.7389, "lng": -72.6489},{"id": 301, "lat": -33.4027, "lng": -70.5304},{"id": 302, "lat": -38.7277, "lng": -72.6333},{"id": 303, "lat": -38.7277, "lng": -72.6333},{"id": 304, "lat": -38.7277, "lng": -72.6333},{"id": 305, "lat": -38.7277, "lng": -72.6333},{"id": 306, "lat": -33.4329, "lng": -70.612},{"id": 307, "lat": -33.4293, "lng": -70.594},{"id": 308, "lat": -33.4053, "lng": -70.5329},{"id": 309, "lat": -33.4076, "lng": -70.5493},{"id": 310, "lat": -33.3823, "lng": -70.5455}]

for sensor in sensors:
    sensor["data"] = []
    for d in range(288):
        temp = random.randint(5,32)
        humd = random.randint(20,80)

        hour = str(int(d*24/288))
        if len(hour) == 1:
            hour = "0" + hour;

        minute = str((d*5)%60)
        if len(minute) == 1:
            minute = "0" + minute;

        sensor["data"].append({
            "Tint": temp,
            "Text": temp - random.randint(0,7),
            "Hint": humd,
            "Hext": humd + random.randint(-30,30),
            "Co2": random.randint(10,90),
            "Ruid": random.randint(10,50),
            "Pm10": random.randint(0,10),
            "Pm25": random.randint(0,25),
            "Powr": random.randint(100,500),
            "Egy": random.randint(100,1000),
            "date": "13-05-2017 " + hour + ":" + minute
        })
    print(sensor["id"])
    
json_data = json.dumps(sensors)


file = open("sensors.json", "w")
file.write(json_data)
file.close()

print("End program")
