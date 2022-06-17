# 랜덤한 배열 정렬에 걸리는 시간 평균, 표준편차 구하기
import matplotlib.pyplot as plt
import math

bubble1 = [0.0, 0.000997781753540039, 0.0030281543731689453, 0.011929512023925781, 0.0488736629486084, 0.10271716117858887, 0.30322980880737305, 1.0562279224395752, 4.424956321716309, 17.751071453094482, 72.8434271812439, 371.5171010494232] 
select1 = [0.0, 0.0, 0.0012869834899902344, 0.004987955093383789, 0.020984649658203125, 0.09839415550231934, 0.4114534854888916, 1.545724630355835, 6.293830871582031, 25.773048639297485, 95.71008658409119, 349.1743576526642] 
insert1 = [0.0, 0.0, 0.0009968280792236328, 0.003989458084106445, 0.018949031829833984, 0.08580899238586426, 0.2971665859222412, 1.3589494228363037, 5.561832666397095, 23.175252199172974, 92.60205221176147, 333.5210590362549]
shell1 = [0.0, 0.0, 0.0, 0.0009975433349609375, 0.0009965896606445312, 0.003989458084106445, 0.013003110885620117, 0.03586459159851074, 0.07380390167236328, 0.22045588493347168, 0.533501386642456, 1.131126880645752] 
heap1 = [0.0, 0.0, 0.0009868144989013672, 0.0, 0.0, 0.0, 0.0009963512420654297, 0.0020041465759277344, 0.00399327278137207, 0.007979869842529297, 0.01790022850036621, 0.03889608383178711]
quick1 = [0.0, 0.0, 0.0, 0.000997781753540039, 0.0, 0.0019943714141845703, 0.0019943714141845703, 0.006175041198730469, 0.012774467468261719, 0.026966094970703125, 0.057805776596069336, 0.14661026000976562] 

bubble2 = [0.0, 0.0, 0.0009646415710449219, 0.0029897689819335938, 0.013963699340820312, 0.09175539016723633, 0.27031731605529785, 1.2805776596069336, 4.924021482467651, 18.91142463684082, 82.76964449882507, 339.21847891807556]
select2 = [0.0, 0.0009517669677734375, 0.002513408660888672, 0.006163597106933594, 0.025973081588745117, 0.0766446590423584, 0.30821967124938965, 1.240480661392212, 4.83732795715332, 20.921674489974976, 80.52227759361267, 325.2075004577637]
insert2 = [0.0, 0.0, 0.003040313720703125, 0.00917196273803711, 0.030724048614501953, 0.06776714324951172, 0.28926730155944824, 1.1678767204284668, 4.731773853302002, 20.60449242591858, 174.40455389022827, 761.9442899227142]
shell2 = [0.0, 0.0006313323974609375, 0.0004279613494873047, 0.0009369850158691406, 0.004227161407470703, 0.010729789733886719, 0.02692723274230957, 0.09024477005004883, 0.22292208671569824, 0.6364412307739258, 1.5081963539123535, 2.624408006668091]
heap2 = [0.0, 0.0, 0.0, 0.0, 0.0010330677032470703, 0.0019567012786865234, 0.003147125244140625, 0.007862567901611328, 0.015033960342407227, 0.025779008865356445, 0.05186605453491211, 0.15956926345825195]
quick2 = [0.0009968280792236328, 0.0, 0.0, 0.0010001659393310547, 0.0020339488983154297, 0.003948688507080078, 0.009124994277954102, 0.019796133041381836, 0.04787182807922363, 0.0718076229095459, 0.18055272102355957, 0.4159657955169678]

bubble3 = [0.0, 0.0002269744873046875, 0.0010013580322265625, 0.004030942916870117, 0.025888442993164062, 0.0658721923828125, 0.2969627380371094, 1.2376856803894043, 5.099444627761841, 45.91790819168091, 179.02449989318848, 482.4088726043701]
select3 = [0.0, 0.0, 0.0020020008087158203, 0.005019426345825195, 0.01994609832763672, 0.07079362869262695, 0.31019091606140137, 1.2048132419586182, 4.9645140171051025, 19.743010997772217, 87.49640035629272, 595.7249143123627]
insert3 = [0.0, 0.0009965896606445312, 0.0020291805267333984, 0.007940053939819336, 0.04890704154968262, 0.19348764419555664, 0.8606553077697754, 3.25989031791687, 13.258170127868652, 56.089675188064575, 222.08257722854614, 719.4359652996063]
shell3 = [0.0, 0.0, 0.0014264583587646484, 0.000568389892578125, 0.001051187515258789, 0.0039844512939453125, 0.010111093521118164, 0.030781030654907227, 0.06781721115112305, 0.18449878692626953, 0.5116350650787354, 1.295902967453003]
heap3 = [0.0, 0.0, 0.000993967056274414, 0.0009984970092773438, 0.0009970664978027344, 0.0010020732879638672, 0.0009975433349609375, 0.001993894577026367, 0.003997802734375, 0.008933305740356445, 0.018981456756591797, 0.046868324279785156]
quick3 = [0.0, 0.0, 0.0, 0.0010006427764892578, 0.001004934310913086, 0.0029909610748291016, 0.003953456878662109, 0.00797891616821289, 0.01795339584350586, 0.03612112998962402, 0.08259987831115723, 0.16035747528076172]

bubble =[]
select =[]
insert =[]
shell =[]
heap =[]
quick =[]

arr_data = []
for i in range(5, 17):
    n = int(math.pow(2,i))
    arr_data.append(n)
    
for i in range(len(bubble1)):
    bubble.append((bubble1[i]+bubble2[i]+bubble3[i])/3)
    select.append((select1[i]+select2[i]+select3[i])/3)
    insert.append((insert1[i]+insert2[i]+insert3[i])/3)
    shell.append((shell1[i]+shell2[i]+shell3[i])/3)
    heap.append((heap1[i]+heap2[i]+heap3[i])/3)
    quick.append((quick1[i]+quick2[i]+quick3[i])/3)
    
bubble_v =[]
select_v =[]
insert_v =[]
shell_v =[]
heap_v =[]
quick_v =[]
for i in range(len(bubble1)):
    bubble_v.append(math.sqrt(math.pow(bubble1[i]-bubble[i],2)+math.pow(bubble2[i]-bubble[i],2)+math.pow(bubble3[i]-bubble[i],2))/2)
    select_v.append(math.sqrt(math.pow(select1[i]-select[i],2)+math.pow(select2[i]-select[i],2)+math.pow(select3[i]-select[i],2))/2)
    insert_v.append(math.sqrt(math.pow(insert1[i]-insert[i],2)+math.pow(insert2[i]-insert[i],2)+math.pow(insert3[i]-insert[i],2))/2)
    shell_v.append(math.sqrt(math.pow(shell1[i]-shell[i],2)+math.pow(shell2[i]-shell[i],2)+math.pow(shell3[i]-shell[i],2))/2)
    heap_v.append(math.sqrt(math.pow(heap1[i]-heap[i],2)+math.pow(heap2[i]-heap[i],2)+math.pow(heap3[i]-heap[i],2))/2)
    quick_v.append(math.sqrt(math.pow(quick1[i]-quick[i],2)+math.pow(quick2[i]-quick[i],2)+math.pow(quick3[i]-quick[i],2))/2)

print(bubble_v, select_v, insert_v, shell_v, heap_v, quick_v)

plt.plot(arr_data, bubble)
plt.plot(arr_data, select)
plt.plot(arr_data, insert)
plt.plot(arr_data, shell)
plt.plot(arr_data, heap)
plt.plot(arr_data, quick)
plt.title('random avg')
plt.xlabel("data") 
plt.ylabel("time")
plt.show()

plt.plot(arr_data, bubble_v)
plt.plot(arr_data, select_v)
plt.plot(arr_data, insert_v)
plt.plot(arr_data, shell_v)
plt.plot(arr_data, heap_v)
plt.plot(arr_data, quick_v)
plt.title('standard deviation')
plt.xlabel("data") 
plt.ylabel("time")
plt.show()