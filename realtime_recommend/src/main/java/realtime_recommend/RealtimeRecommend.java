package main.java.realtime_recommend;

/**
 * Created by uxin on 2018/5/2.
 *
 *      完成实时行个性化推荐
 *      策略如下：
 *          1.从Hbase中读取每天进行一次提取的视频特征向量
 *          2.从Hbase中读取实时描绘的用户画像数据
 *          3.从Hive中读取用户最近一个月之内观看的视频记录数据
 *          4.通过以上3方面的数据，来计算视频之间的相似度，从而决定推荐序列
 *      相似度的计算法则：
 *              兴趣分布比例*观看时长上的时间衰减*观看时间上的时间衰减*视频特征向量的距离
 *
 *                          (-120s/interval)*ln(2)    (-t/30d)*ln(2)
 *             兴趣分布比例*e                        *e               *(归一化以后的距离)
 *
 */
public class RealtimeRecommend {

}
