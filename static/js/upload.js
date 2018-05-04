$("#pic").hide();
function uploadFile() {
    var form = document.getElementById('upload'),
        formData = new FormData(form);
    $.ajax({
        url:"/uploadfile/",
        type:"post",
        data:formData,
        processData:false,
        contentType:false,
        success:function(res){
            if(res){
                alert("上传成功！");
            }
            console.log(res);
        },
        error:function(err){
            alert("网络连接失败,稍后重试", err);
        }});
}