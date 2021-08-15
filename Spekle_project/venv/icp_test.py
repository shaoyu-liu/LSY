import numpy as np
import open3d as o3d
import copy

def draw_registration_result(source, target, transformation):
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    source_temp.paint_uniform_color([1, 0.706, 0])
    target_temp.paint_uniform_color([0, 0.651, 0.929])
    source_temp.transform(transformation)
    o3d.visualization.draw_geometries([source_temp, target_temp],
                                      zoom=0.4459,
                                      front=[0.9288, -0.2951, -0.2242],
                                      lookat=[1.6784, 2.0612, 1.4451],
                                      up=[-0.3402, -0.9189, -0.1996])

source = o3d.io.read_point_cloud("F:/img3/ptCloud4.ply")
target = o3d.io.read_point_cloud("F:/img3/ptCloud5.ply")
threshold = 0.02
trans_init = np.asarray([[-0.78,-0.29,-0.63124077,19.38678607],   # 4x4 identity matrix，这是一个转换矩阵，
                         [-0.2798522,0.95700218,-0.07635169,12.31399072],   # 象征着没有任何位移，没有任何旋转，我们输入
                         [-0.61745829,-0.11852031,0.77762343,21.60276813],   # 这个矩阵为初始变换
                         [0,0,0,1]])
draw_registration_result(source, target, trans_init)

reg_p2p = o3d.pipelines.registration.registration_icp(source, target, threshold, trans_init,
        o3d.pipelines.registration.TransformationEstimationPointToPoint(),
        o3d.pipelines.registration.ICPConvergenceCriteria(max_iteration = 30))
print(reg_p2p)
print("Transformation is:")
print(reg_p2p.transformation)
draw_registration_result(source, target, reg_p2p.transformation)

