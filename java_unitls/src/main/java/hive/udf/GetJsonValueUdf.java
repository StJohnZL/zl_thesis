package hive.udf;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import org.apache.hadoop.hive.ql.exec.UDF;

/**
 * Created by uxin on 2018/5/6.
 *
 *      自定义hive udf 实现从json串中获取指定字段的value
 *
 */
public class GetJsonValueUdf extends UDF {

    /**
     *      提取json指定字段的value
     */
    public String evaluate(String jsonStr, String fieldStr){

        JSONObject jsonObj = (JSONObject) JSON.parse(jsonStr) ;

        if (jsonObj!=null){
            String value = jsonObj.getString(fieldStr) ;
            if (value != null) {
                return value;
            } else return null ;
        }

        return null;
    }

//    public static void main(String[] args) {
//        GetJsonValueUdf get = new GetJsonValueUdf();
//        String value = get.evaluate("{'id':'1'}", "i") ;
//        System.out.println(value);
//    }

}
