$(document).ready(function(){
   
   /* EDIT HABIT'S TITLE OR DESCRIPTION */
   // Handler to reset
   var resetHandler = function(event){
      var el = event.data.element;
      var old_data = event.data.old_data;
      el.html(old_data);
      el.on('dblclick', editHandler);
   }
   
   // Handler to send Ajax request
   var requestHandler = function(event){
      var el = event.data.element;
      var new_data = el.find('#newData').val();
      var old_data = event.data.old_data;
      var edit_type = 'desc';
      if(el.attr('id') == 'habitTitle'){
         edit_type = 'title';
      }
      var habit_slug = el.attr('data-slug');
      
      // If there is some new data sends Ajax request
      // and stores response in new_data
      if(new_data != '' && new_data != old_data){
         $.ajax({
            type: "GET",
            url: "/habits/update_habit/edit_title/", 
            data: {slug: habit_slug, new_data: new_data, edit_type: edit_type},
            success: function(result){
               new_data = result;
            },
            error: function(xhr, ajaxOptions, thrownError){
               new_data = old_data; // Resets old title in case of error
            }
         });
         
         // Write the new data in HTML element
         el.html(new_data);
      
         // Resets event handler for double click
         el.on('dblclick', editHandler);
      }
   }
   
   // Handler to start edit
   var editHandler = function(){
      var el = $(this);
      var btn = $('<button id="changeBtn">OK</button>');
            
      // Removes event handler to prevent double click event while editing 
      el.off('dblclick');
      
      var habit_slug = el.attr('data-slug');
      var old_data = el.html().trim();
      
      // Adds text field to enter the new title
      if(el.attr('id') == 'habitTitle'){
         el.html('<input id="newData" type="text" value="' + old_data + '"/>');
      }
      else{
         el.html('<textarea id="newData">' + old_data + '</textarea>');
      }
      
      // Sets focus on the input element and adds button
      $('#newData').focus().after(btn);
      
      // Double clicking outside the text field cancels the operation
      $('#newData').on('blur', {element:el, old_data:old_data}, resetHandler);
      
      // Clicking the button sends an Ajax request
      $('#changeBtn').on('mousedown', {element:el, old_data:old_data}, requestHandler);
   };
   
   // Binds event handler to the elements
   $('#habitTitle').on('dblclick', editHandler);
   $('#habitDesc').on('dblclick', editHandler);
   
   
   /* TOGGLES DAY VALUE */
   $('.day').click(function(){
      var day = $(this);
      var day_id = $(this).attr('id');
      day_id = day_id.substr(day_id.indexOf('_') + 1);
      var habit_slug = $(this).parents('#xTable').attr('data-slug');
      $.ajax({
         type: "GET",
         url: "/habits/update_habit/toogle_day/", 
         data: {slug: habit_slug, day_id: day_id},
         success: function(result){
            var new_value = result.new_value;
            if(new_value == 1){
               day.html("X");
            }
            else{
               day.html("O");
            }
         },
         error: function(xhr, ajaxOptions, thrownError){
            return;
         }
      });
   });
   
   /* SET TODAY VALUE */
   $('.todayBtn').click(function(){
      var el = $(this);
      var habit_slug = el.attr('data-slug');
      
      $.ajax({
         type: "GET",
         url: "/habits/update_habit/set_today/", 
         data: {slug: habit_slug},
         success: function(result){
            if(result.today == 1){
               el.prop('disabled', true);
            }
         },
         error: function(xhr, ajaxOptions, thrownError){
            return;
         }
      });
   });
});

