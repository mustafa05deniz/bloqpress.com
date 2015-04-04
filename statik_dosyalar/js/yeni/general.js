jQuery.noConflict();
(function ($) {

	jQuery(window).load(function () {
		// add a class so we know JavaScript is supported
		jQuery('html').addClass("js");
		jQuery('html').removeClass("no-js");
	});

    // Initialisations ..
    jQuery(document).ready(function () {
        if ((navigator.userAgent.match(/iPhone/i)) || (navigator.userAgent.match(/Android/i)) || (navigator.userAgent.match(/Blackberry/i))) {
            jQuery("body").addClass("mobiledevice");
            var isMobile = true;
        };
        
        if ( navigator.userAgent.match(/iPad/i) ) {
            jQuery("body").addClass("ipad");
            var isIpad = true;
        };
        
        // contact thanks
        if (jQuery("body").is(".page-template-template-submit-php")) {
        	  jQuery(function() {
        	      if ( document.location.href.indexOf('#thanks') > -1 ) {
        	          jQuery('#thanks-overlay').delay(1000).fadeIn();
        	      }
        	  });
        	  jQuery('a.thanks-close').on("click", function(e){
        	  	e.preventDefault();
        	      jQuery('#thanks-overlay').fadeOut();
        });
        }
        
        // get screen width
        currWidth = window.innerWidth;
        
        // superfish menus
        jQuery(function () {
                jQuery('header nav ul').superfish({
                    autoArrows: false,
                    dropShadows: false,
                    delay: 100
                });
        });
        
        // get logo data
        $logo = jQuery('img.logo');
        $logoSrc = $logo.attr("src");
        $logo1440 = $logo.attr("data-fullsrc");
        
        // switch logo for enhanced layout
        if(currWidth >= 1440 ) {
        	stickyLists();
        	$logo.attr("src" , $logo1440);
        	jQuery('.asides-holder').addClass("sticky");
     		jQuery('.asides-holder').css("margin-top" , 55);
        }
        
        // sticky great lists
        function stickyLists() {
       	 	if (jQuery("body").is(".single")) {
		        if(currWidth < 1440 ) {
	            	jQuery(".asides-holder").css("margin-top" , 0);
	            	$sidebar = "";
	            } else {
	            	$sidebar   = jQuery(".asides-holder.sticky"), 
	            	        $window    = jQuery(window),
	            	        offset     = $sidebar.offset(),
	            	        fCombinedHeight = ((jQuery(".comments").height() + jQuery("footer").height())*2),
	            	        docHeight = jQuery(document).height(),
	            	        topPadding = 95;
	            	
	            	    $window.scroll(function() {
	            	    	var pos = jQuery( ".sharing" ).position(); 
	            	        if ($window.scrollTop() > offset.top) {
	            	            $sidebar.stop().css("margin-top",($window.scrollTop() - offset.top + topPadding));
	            	        } else {
	            	            $sidebar.stop().css("margin-top",55);
	            	        }
	            	        // docHeight - fCombinedHeight
	            	        if( ($window.scrollTop()) > (pos.top-350) ) {
	            	         	$sidebar.hide();
	            	        }
	            	        else {
	            	        	$sidebar.show();
	            	        }
	            	    });
	            }
	        }    
        }
        stickyLists();
        
        jQuery(window).resize(function () {
         	currWidth = window.innerWidth;
        	    // switch logo for enhanced layout
         	if(currWidth >= 1440 ) {
            	$logo.attr("src" , $logo1440);
        	 	if (jQuery("body").is(".single")) {
	        		jQuery('.asides-holder').addClass("sticky");
	        		jQuery('.asides-holder').css("margin-top" , 55);
	            	stickyLists();
	            }	
         	} else {
            	$logo.attr("src" , $logoSrc);
       	 		if (jQuery("body").is(".single")) {
	            	jQuery('.asides-holder').removeClass("sticky");
	         		jQuery('.asides-holder').css("margin-top" , 0);
	            	stickyLists();
	            }	
         	}
        });
        
        // stop scrollbar for iFrame loaded at top of body for Google Ads
        jQuery("iframe").first().css("left: -99999em");
        
        //mobileMenu 
        	var navContents = jQuery("header nav.top-nav").html();
        	jQuery("nav.mobile").html(navContents);
        	
        	jQuery(".mobile-more").on("click", function(e) {
        		e.preventDefault();
	        	jQuery('nav.mobile ul#menu-main').removeAttr("class");
        		jQuery(this).toggleClass("active");
        		jQuery("nav.mobile").fadeToggle();
        	});
        	
        	// mobile more menu
        	var moreContents = jQuery("header nav.top-nav li.load-none ul").html();
        	jQuery("nav.more").html("<ul>" + moreContents + "</ul>");
        	
        	jQuery(".more-more").on("click", function(e) {
        		e.preventDefault();
        		jQuery(this).toggleClass("active");
        		jQuery("nav.more").fadeToggle();
        	});
        	
        	jQuery(".mobile-tab.new-lists").on("click", function(e) {
        		e.preventDefault();
        		jQuery(".mobile-tab").removeClass("active");
        		jQuery("section.new").removeClass("hide").addClass("show");
        		jQuery("section.current").removeClass("show").addClass("hide");
        		jQuery(this).addClass("active");
        	});
        	
        	jQuery(".mobile-tab.categories").on("click", function(e) {
        		e.preventDefault();
				jQuery(".mobile-tab").removeClass("active");
				jQuery("section.current").removeClass("hide").addClass("show");
				jQuery("section.new").removeClass("show").addClass("hide");
				jQuery(this).addClass("active");
        	});
       
	    // append posts onto menu display 
	    jQuery('header nav.top-nav ul ul').append('<li class="nav-posts" />');
	    
	    // ajax them based on URL
	    jQuery(".load-entertainment ul li.nav-posts").load("/navposts-entertainment/", function(response, status, xhr) {
	      if (status == "error") {
	        var msg = "Sorry but there was an error: ";
	        jQuery(".load-entertainment ul li.nav-posts").css("color" , "grey").html(msg + xhr.status + " " + xhr.statusText);
	      }
	    });
	    jQuery(".load-science ul li.nav-posts").load("/navposts-science/", function(response, status, xhr) {
	      if (status == "error") {
	        var msg = "Sorry but there was an error: ";
	        jQuery(".load-science ul li.nav-posts").css("color" , "grey").html(msg + xhr.status + " " + xhr.statusText);
	      }
	    });
	    jQuery(".load-general ul li.nav-posts").load("/navposts-general/", function(response, status, xhr) {
	      if (status == "error") {
	        var msg = "Sorry but there was an error: ";
	        jQuery(".load-general ul li.nav-posts").css("color" , "grey").html(msg + xhr.status + " " + xhr.statusText);
	      }
	    });
	    jQuery(".load-lifestyle ul li.nav-posts").load("/navposts-lifestyle/", function(response, status, xhr) {
	      if (status == "error") {
	        var msg = "Sorry but there was an error: ";
	        jQuery(".load-lifestyle ul li.nav-posts").css("color" , "grey").html(msg + xhr.status + " " + xhr.statusText);
	      }
	    });
	    jQuery(".load-society ul li.nav-posts").load("/navposts-society/", function(response, status, xhr) {
	      if (status == "error") {
	        var msg = "Sorry but there was an error: ";
	        jQuery(".load-society ul li.nav-posts").css("color" , "grey").html(msg + xhr.status + " " + xhr.statusText);
	      }
	    });
	    jQuery(".load-weird ul li.nav-posts").load("/navposts-weird/", function(response, status, xhr) {
	      if (status == "error") {
	        var msg = "Sorry but there was an error: ";
	        jQuery(".load-weird ul li.nav-posts").css("color" , "grey").html(msg + xhr.status + " " + xhr.statusText);
	      }
	    });
	    
	    // tabs
	    jQuery(".choice-popular a, .choice-recent a").on("click", function() {
		    var tabClick = jQuery(this).parent().attr("class");
	    	jQuery(".choice-popular a, .choice-recent a").removeClass();	    
		    
	    	jQuery(".choice-popular a, .choice-recent a").removeClass();
		    if(tabClick == "choice-recent") {
		    	jQuery(".tab-popular").hide();
		    	jQuery(".tab-recent").show();
		    }
		    if(tabClick == "choice-popular") {
		    	jQuery(".tab-popular").show();
		    	jQuery(".tab-recent").hide();
		    }
	    	jQuery(this).addClass("tab-active");
	    });

	    // category dropdown
	    catClick = false;
	    jQuery(".choice-categories ul").hide();
	    jQuery(".choice-categories .head-title a").on("click", function(e){
			e.preventDefault();
			if(catClick) {
				jQuery(this).removeClass("active");
				jQuery(".choice-categories ul").fadeOut();
				catClick = false;			
			} else {
				jQuery(this).addClass("active");
				jQuery(".choice-categories ul").addClass("active");
				jQuery(".choice-categories ul").fadeIn();
				catClick = true;			
			}
		});
		
		// filter by category
		jQuery(".choice-categories ul li a").on("click", function(e){
			e.preventDefault();
			jQuery('.choice-categories ul li a').removeClass();
			jQuery(".choice-categories ul").fadeOut();
			var getHash = jQuery(this).attr("href");
			var getHashUrl = getHash.slice(1);
			
			//find out what is active
			var choicePopular = jQuery(".choice-popular a").attr("class");
			var choiceRecent = jQuery(".choice-recent a").attr("class");
			
			if(choicePopular == "tab-active") {
				$tabLoad = '.tab-popular';
				getHashUrl = getHashUrl+"-popular";
			}
			if(choiceRecent == "tab-active") {
				$tabLoad = '.tab-recent';
			}
			jQuery($tabLoad).load("/" + getHashUrl + "/", function(response, status, xhr) {
				
			  if (status == "error") {
			    var msg = "Sorry but there was an error: ";
			    jQuery($tabLoad).html(msg + xhr.status + " " + xhr.statusText);
			  }
			});
			jQuery(this).parent().removeClass("active");
			jQuery('.choice-categories .head-title a').removeClass("active");
			catClick = false;
		});
		
		// share button
		isShare = false; 
		jQuery("a.btn.share").on("click", function(e) {
			e.preventDefault();
			isShare = true;
			jQuery(this).toggleClass("active");
			jQuery(this).next().toggleClass("active");
		});
		jQuery('html').on("click", function() {
			if(isShare) {
				jQuery('a.btn.share, ul.post-share').removeClass("active");
			}
		});
		jQuery('a.btn.share').click(function(event){
		    event.stopPropagation();
		});
		
		//  FitVids
		jQuery("article").fitVids();
		
		//search click
		jQuery('.search-top-reveal').hide();
		jQuery('a.search-top').on("click", function(e) {
			e.preventDefault();
			jQuery(this).toggleClass("active");
			jQuery('.search-top-reveal').addClass("active");
			jQuery('.search-top-reveal input').val("");
			jQuery('.search-top-reveal').fadeToggle();
		});
		
		// Follow 
		jQuery('.follow-reveal').hide();
		jQuery('.follow-top a.follow').on("click", function(e) {
			e.preventDefault();
			jQuery('.follow-reveal').addClass("active");
			jQuery(this).parent().toggleClass("active");
			jQuery('.follow-reveal input.emailaddress').val("");
			jQuery('.follow-reveal').fadeToggle();
		});
		
		// switch retina logo
		if (window.devicePixelRatio >= 1.5) {
			jQuery(".footer-logo").attr("src" , siteUrl + "assets/img/logo-footer@2x.png");
		} 
    
        //strip image sizes
        jQuery('article img').each(function () {
            jQuery(this).removeAttr('width')
            jQuery(this).removeAttr('height');
        });
        
        // polyfill placeholder text
        if ( (jQuery('html').hasClass("oldie")) || (jQuery('html').hasClass("ie9")) ) {
            jQuery('[placeholder]').focus(function () {
                var input = jQuery(this);
                if (input.val() == input.attr('placeholder')) {
                    input.val('');
                    input.removeClass('placeholder');
                }
            }).blur(function () {
                var input = jQuery(this);
                if (input.val() == '' || input.val() == input.attr('placeholder')) {
                    input.addClass('placeholder');
                    input.val(input.attr('placeholder'));
                }
            }).blur().parents('form').submit(function () {
                jQuery(this).find('[placeholder]').each(function () {
                    var input = $(this);
                    if (input.val() == input.attr('placeholder')) {
                        input.val('');
                    }
                })
            });
        }
        
        // last / first of type polyfill
        if ( jQuery('html').hasClass("oldie") ) {
        	jQuery('nav.top-nav ul li').last().addClass("last");
        	jQuery('footer .social a').first().addClass("first");        	
        }
    });
    // .. Initialisations
})(jQuery);