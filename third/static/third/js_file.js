function temp(){
    alert("temp 입니다.");
}


function create_restaurant(){
    let create_rest_url = $("#create_rest_url").val();
    let restaurant_list_url = $("#restaurant_list_url").val();
    let form_info = $('#create_rest_form')[0];

    let form_data = new FormData(form_info);
    console.log("form_data", form_data);

    let input_tags = form_info.getElementsByTagName('input');
    for(let i=0; i<input_tags.length; i++){
        let tag_name = input_tags[i].name;
        let tag_value = input_tags[i].value;
        if(     (tag_name == 'name' && tag_value == '')
            ||  (tag_name == 'address' && tag_value == '')){
            return alert("이름 혹은 주소정보 입력 부탁드립니다.");
        }
    }

    $.ajax({
        type        : 'POST',
        enctype     : 'multipart/form-data',
        url         : create_rest_url,
        data        : form_data,
        contentType : false,
        processData : false,
        success     : function (data) {
            if(data.result == 'SUCCESS'){
                alert("등록 완료하였습니다.");
                window.location.href = restaurant_list_url;
            }else{
                alert("등록 실패");
            }
        },
        error       : function (error) {
            console.log("error", error);
        }
    });
}


function delete_restaurant(){
    if(!confirm('정말 삭제하시겠습니까?')) return;

    let delete_rest_url = $("#delete_rest_url").val();
    let restaurant_id = $("#restaurant_id").val();
    let restaurant_list_url = $("#restaurant_list_url").val();
    let csrf_token = $("#csrf_token").val();

    let data_info = {
        'restaurant_id' : restaurant_id
    }
    $.ajax({
        type        : 'POST',
        url         : delete_rest_url,
        headers     : {
            "X-CSRFToken" : csrf_token
        },
        data        : JSON.stringify(data_info),
        contentType : false,
        processData : false,
        success     : function (data) {
            if(data.result == 'SUCCESS'){
                alert("삭제 완료하였습니다.");
                window.location.href = restaurant_list_url;
            }else{
                alert("삭제 실패");
            }
        },
        error       : function (error) {
            console.log("error", error);
        }
    });
}


function update_restaurant(){
    let update_rest_url = $("#update_rest_url").val();
    let restaurant_id = $("#restaurant_id").val();
    let restaurant_list_url = $("#restaurant_list_url").val();
    let form_info = $('#update_rest_form')[0];
    let form_data = new FormData(form_info);

    let input_tags = form_info.getElementsByTagName('input');
    for(let i=0; i<input_tags.length; i++){
        let tag_name = input_tags[i].name;
        let tag_value = input_tags[i].value;
        if(     (tag_name == 'name' && tag_value == '')
            ||  (tag_name == 'address' && tag_value == '')){
            return alert("이름 혹은 주소정보 입력 부탁드립니다.");
        }
    }

    $.ajax({
        type        : 'POST',
        enctype     : 'multipart/form-data',
        url         : update_rest_url,
        data        : form_data,
        contentType : false,
        processData : false,
        success     : function (data) {
            if(data.result == 'SUCCESS'){
                alert("수정 완료하였습니다.");
                window.location.href = restaurant_list_url;
            }else{
                alert("수정 실패");
            }
        },
        error       : function (error) {
            console.log("error", error);
        }
    });
}