$( document ).ready(function() {
    $('.actions').hide();
});


function paid(id_function){
    if (confirm('¿Está seguro que desea marcarlo como inscripto?')) {
        var buscado = "input:checkbox[value='"+id_function+"']";
        console.log(buscado);
        $("input:checkbox").attr("checked", false);
        $(buscado)[0].checked = true;
        $("select[name='action']").val("make_paid");
        $("button[name='index']").click();
    } else {
        return false;
    }


}
