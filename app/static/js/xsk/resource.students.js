
$("#mytable").bootstrapTable({ // 对应table标签的id
    url: "/resources/show/students/", // 获取表格数据的url
    cache: false, // 设置为 false 禁用 AJAX 数据缓存， 默认为true
    toolbar : "#toolbar",
    striped: true, //表格显示条纹，默认为false
    pagination: true, // 在表格底部显示分页组件，默认false
    pageList: [10, 20], // 设置页面可以显示的数据条数
    pageSize: 10, // 页面数据条数
    pageNumber: 1, // 首页页码
    clickToSelect: true,
    sidePagination: 'server', // 设置为服务器端分页
    queryParams: function(params) { // 请求服务器数据时发送的参数，可以在这里添加额外的查询参数，返回false则终止请求
        return {
            pageSize: params.limit, // 每页要显示的数据条数
            offset: params.offset, // 每页显示数据的开始行号
            sort: params.sort, // 要排序的字段
            sortOrder: params.order, // 排序规则
            // dataId: $("#dataId").val() // 额外添加的参数
        }
    },
    sortName: 'id', // 要排序的字段
    sortOrder: 'desc', // 排序规则
    columns: [{
            checkbox: true, // 显示一个勾选框
            align: 'center' // 居中显示
        }, {
            field: 'student_name',
            title: '学生姓名',
            align: 'center',
            valign: 'middle'
        }, {
            field: 'student_age',
            title: '年龄',
            align: 'center',
            valign: 'middle'
        },
        {
            field: 'student_sex',
            title: '性别',
            align: 'center',
            valign: 'middle',
           
        },
        {
            field: 'student_phone',
            title: '电话',
            align: 'center',
            valign: 'middle'
        },
        {
            field: 'student_ID',
            title: '身份证号',
            align: 'center',
            valign: 'middle'
        },
        {
            field: 'student_info',
            title: '备注',
            align: 'center',
            valign: 'middle'
        },
        {
            field: 'student_create',
            title: '创建时间',
            align: 'center',
            valign: 'middle'
        },
        // {
        //     field: 'calcMode',
        //     title: '计算方式',
        //     align: 'center',
        //     valign: 'middle',
        //     formatter: function (value, row, index){ // 单元格格式化函数
        //         var text = '-';
        //         if (value == 1) {
        //             text = "方式一";
        //         } else if (value == 2) {
        //             text = "方式二";
        //         } else if (value == 3) {
        //             text = "方式三";
        //         } else if (value == 4) {
        //             text = "方式四";
        //         }
        //         return text;
        //     }
        // }, 
        // {
        //     title: "操作",
        //     align: 'center',
        //     valign: 'middle',
        //     width: 160, // 定义列的宽度，单位为像素px
        //     formatter: function(value, row, index) {
        //         return '<button class="btn btn-primary btn-sm" onclick="del(\'' + row.student_id + '\')">删除</button>';
        //     }
        // }
    ],
    onLoadSuccess: function() { //加载成功时执行
        console.info("加载成功");
    },
    onLoadError: function() { //加载失败时执行
        console.info("加载数据失败");
    },

})

function del(id){
    alert("delete!")
}


//使用getSelections即可获得，row是json格式的数据
var $table = $('#mytable'),
    $choices = $('#mychoices');

$(function () {
    $choices.click(function () {
        alert('getSelections: ' + JSON.stringify($table.bootstrapTable('getSelections')));
    });
});



