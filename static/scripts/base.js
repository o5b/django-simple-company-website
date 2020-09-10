"use strict";

$(function () {
  var BODY = {
    $body: $('body'),
    $menu: $('.js-menu'),
    $scroll: $('.js-menu-scroll'),
    $translator: $('.js-translator'),
    freeze: function freeze() {
      var bodyWidth = this.$body.innerWidth();
      this.$body.addClass('body-freeze');
      this.$menu.css('marginRight', (this.$body.css('marginRight') ? '+=' : '') + (this.$body.innerWidth() - bodyWidth));
      this.$scroll.css('marginRight', (this.$body.css('marginRight') ? '+=' : '') + (this.$body.innerWidth() - bodyWidth));
      this.$translator.css('marginRight', (this.$body.css('marginRight') ? '+=' : '') + (this.$body.innerWidth() - bodyWidth));
      this.$body.css('marginRight', (this.$body.css('marginRight') ? '+=' : '') + (this.$body.innerWidth() - bodyWidth));
    },
    unfreeze: function unfreeze() {
      var bodyWidth = this.$body.innerWidth();
      this.$body.removeClass('body-freeze');
      this.$menu.css('marginRight', "-=".concat(bodyWidth - this.$body.innerWidth()));
      this.$scroll.css('marginRight', "-=".concat(bodyWidth - this.$body.innerWidth()));
      this.$translator.css('marginRight', "-=".concat(bodyWidth - this.$body.innerWidth()));
      this.$body.css('marginRight', "-=".concat(bodyWidth - this.$body.innerWidth()));
    }
  };
  var MENU = {
    $menu: $('.js-menu'),
    init: function init() {
      var _this = this;

      var $menuBtn = $('.js-menu-btn');
      $menuBtn.on('click', function (e) {
        e.preventDefault();

        _this.$menu.addClass('menu-show');

        BODY.freeze();
      });
      var $menuClose = $('.js-menu-close');
      $menuClose.on('click', function (e) {
        e.preventDefault();

        _this.$menu.removeClass('menu-show');

        setTimeout(function () {
          BODY.unfreeze();
        }, 500);
      });
    }
  };
  MENU.init();
  var MENUSCROLL = {
    menuScroll: $('.js-menu-scroll'),
    init: function init() {
      window.addEventListener('scroll', this.menuScrollToggle.bind(this));
      this.menuScrollToggle();
    },
    menuScrollToggle: function menuScrollToggle() {
      if (window.pageYOffset > 200) {
        this.menuScroll.addClass('scroll-fixed');
      } else {
        this.menuScroll.removeClass('scroll-fixed');
      }
    }
  };
  MENUSCROLL.init();
  var MODAL = {
    init: function init() {
      var $modalBtn = $('.js-modal-btn');
      $modalBtn.on('click', function (e) {
        e.preventDefault();
        var $this = $(e.currentTarget);
        var $modal = $('.js-modal').filter("[data-modal=\"".concat($this.data('target'), "\"]"));
        $modal.addClass('modal-show');
        BODY.freeze();
      });
      var $modalClose = $('.js-modal-close');
      $modalClose.on('click', function (e) {
        e.preventDefault();
        $(e.currentTarget).closest('.js-modal').removeClass('modal-show');
        setTimeout(function () {
          BODY.unfreeze();
        }, 300);
      });
    }
  };
  MODAL.init();
  var SUBNAV = {
    subnav: $('.js-subnav-fixed'),
    subnavHeight: 0,
    anchor: $('.js-subnav-anchor'),
    link: undefined,
    sections: undefined,
    anchorTop: 0,
    anchorBottom: 0,
    generalOffset: 0,
    customGap: 90,
    init: function init() {
      var _this2 = this;

      if (window.innerWidth <= 960) {
        window.addEventListener('scroll', this.subnavScrollToggle.bind(this));
        return;
      }

      this.subnav.fadeIn();

      if (!this.anchor.length) {
        return;
      }

      this.link = $('.js-subnav-link');
      this.sections = this.link.map(function (idx, el) {
        return $(el.getAttribute('href'));
      });
      setTimeout(function () {
        // Delay for correct calc height and offset
        _this2.anchorTop = _this2.anchor.offset().top;
        _this2.anchorBottom = _this2.anchorTop + _this2.anchor.height();
        _this2.subnavHeight = _this2.subnav.height();
        _this2.generalOffset = _this2.anchorTop;

        _this2.checkSubnav();

        window.addEventListener('scroll', _this2.checkSubnav.bind(_this2));
      }, 500);
    },
    checkSubnav: function checkSubnav() {
      var _this3 = this;

      var top = window.pageYOffset || document.documentElement.scrollTop;

      if (this.anchorTop - top < this.customGap && top + this.subnavHeight < this.anchorBottom) {
        this.subnav.addClass('subnav-fixed');
        this.subnav.css('top', this.customGap);
      }

      if (top + this.subnavHeight + this.customGap > this.anchorBottom) {
        this.subnav.removeClass('subnav-fixed');
        this.subnav.css('top', this.anchorBottom - this.subnavHeight - this.generalOffset);
      }

      if (this.anchorTop - top > this.customGap) {
        this.subnav.removeClass('subnav-fixed');
        this.subnav.css('top', 'auto');
      }

      this.sections.each(function (idx, el) {
        if (el.offset().top > top) {
          _this3.link.removeClass('subnav__a-active');

          _this3.link.filter("[href=\"#".concat(el.attr('id'), "\"]")).addClass('subnav__a-active');

          return false;
        }

        return true;
      });
    },
    subnavScrollToggle: function subnavScrollToggle() {
      if (window.pageYOffset > window.innerHeight) {
        this.subnav.addClass('subnav-fixed');
      } else {
        this.subnav.removeClass('subnav-fixed');
      }
    }
  };
  SUBNAV.init();
  var SMOOTHSCROLL = {
    init: function init() {
      $('a[href*="#"]').click(function (e) {
        if (window.location.hostname === e.currentTarget.hostname) {
          var target = $(e.currentTarget.hash);
          target = target.length ? target : $("[id=".concat(e.currentTarget.hash.slice(1), "]"));

          if (target.length) {
            e.preventDefault();
            $('html, body').animate({
              scrollTop: target.offset().top - 80
            }, 1000, function () {
              $(e.currentTarget).blur();
              return true;
            });
          }
        }
      });
    }
  };
  SMOOTHSCROLL.init();
  var SWIPER = {
    init: function init() {
      $('.js-swiper').each(function (idx, el) {
        var $swiper = $(el);
        var dataSwiper = $swiper.data('swiper') || {};
        var defaultParams = {
          direction: 'horizontal',
          slidesPerView: 4,
          spaceBetween: 0,
          roundLengths: true,
          loop: false,
          pagination: {
            el: $swiper.find('.js-swiper-pagination'),
            clickable: true,
            bulletClass: 'arrow__point',
            bulletActiveClass: 'arrow__point-active'
          },
          navigation: {
            prevEl: $swiper.find('.js-swiper-left'),
            nextEl: $swiper.find('.js-swiper-right')
          },
          breakpoints: {
            // when window width is <= 320px
            320: {
              slidesPerView: 1,
              slidesPerGroup: 1
            },
            // when window width is <= 576px
            576: {
              slidesPerView: 2,
              spaceBetween: 10
            },
            // when window width is <= 992px
            992: {
              slidesPerView: 3
            }
          },
          on: {
            init: function init() {
              $swiper.find('.swiper-load').removeClass('swiper-load');
            }
          }
        };
        var params = Object.assign(defaultParams, dataSwiper); // eslint-disable-next-line

        new Swiper($swiper.find('.swiper-container'), params);
      });
    }
  };
  SWIPER.init();
  var PHOTO = {
    init: function init() {
      $('.js-photo').jqPhotoSwipe({
        bgOpacity: 0.7
      });
      $('.js-photo-content').find('a:has(img)').jqPhotoSwipe({
        bgOpacity: 0.7
      });
    }
  };
  PHOTO.init();
  var APPOINTMENT = {
    init: function init() {
      $('a[href="#appointment"]').on('click', function () {
        $('.js-modal-btn[data-target="appointment"]').trigger('click');
      });
      var $detail = $('.js-appointment-detail');
      $('.js-appointment-detail-btn').on('click', function () {
        $detail.slideToggle();
      });
    }
  };
  APPOINTMENT.init();
  var TIPPY = {
    init: function init() {
      $('.js-tippy').each(function (idx, el) {
        var html = document.querySelector(el.getAttribute('data-html')).innerHTML;
        tippy(el, {
          content: html,
          arrow: true,
          theme: 'light',
          arrowTransform: 'scale(2)',
          trigger: 'click'
        });
      });
    }
  };
  TIPPY.init();
  var FORM = {
    init: function init() {
      var $form = $('.js-form');
      $form.on('submit', function (e) {
        e.preventDefault();
        var $this = $(e.currentTarget);
        var $submit = $this.find('[type="submit"]');
        var $successShow = $this.find('.js-form-success-show');
        var $successHide = $this.find('.js-form-success-hide');
        var data = new FormData($this.get(0));
        var submitText = $submit.text();
        $submit.text('Отправляю...');
        $submit.attr('disabled', 'disabled');
        $.ajax({
          url: $this.attr('action'),
          type: $this.attr('method'),
          data: data,
          cache: false,
          processData: false,
          contentType: false
        }).done(function () {
          $successHide.slideUp();
          $successShow.slideDown();

          if ($this.data('goal')) {
            dataLayer.push({
              event: $this.data('goal')
            });
          }
        }).fail(function (res) {
          var message = Object.keys(res.responseJSON).map(function (el) {
            return res.responseJSON[el];
          }).join('\n'); // eslint-disable-next-line

          window.alert("\u0418\u0441\u043F\u0440\u0430\u0432\u044C\u0442\u0435 \u043E\u0448\u0438\u0431\u043A\u0438:\n ".concat(message));
        }).always(function () {
          $submit.removeAttr('disabled');
          $submit.text(submitText);
        });
        return true;
      });
    }
  };
  FORM.init();
  var FLATPICKR = {
    init: function init() {
      $('.js-flatpickr').flatpickr({
        locale: 'ru',
        altInput: true,
        altFormat: 'j F, Y в H:i',
        dateFormat: 'd.m.Y H:i',
        enableTime: true,
        time_24hr: true,
        minDate: 'today',
        minTime: '10:00',
        maxTime: '21:30',
        disable: [function (date) {
          return date.getDay() === 0;
        }]
      });
    }
  };
  FLATPICKR.init();
  var HIGHLIGHT = {
    init: function init() {
      var urlParams = new URLSearchParams(window.location.search);
      var highlight = urlParams.get('highlight');

      if (!highlight) {
        return false;
      }

      var $section = $('section');
      $section.mark(highlight, {
        done: function done() {
          var $results = $section.find('mark');
          var $first = $results.first();

          if ($first.length) {
            setTimeout(function () {
              $('html, body').animate({
                scrollTop: $first.offset().top - 80
              }, 500);
            }, 500);
          }
        }
      });
      return true;
    }
  };
  HIGHLIGHT.init();
  var NIGHT = {
    $button: $('.js-night-btn'),
    $body: $('body'),
    night_start: 20,
    night_end: 8,
    init: function init() {
      var _this4 = this;

      var date = new Date();
      var hours = date.getHours();

      if (localStorage.getItem('night') === 'true') {
        this.addNight();
      }

      if (hours >= this.night_start || hours < this.night_end) {
        if (localStorage.getItem('night') === 'false') {
          if (sessionStorage.getItem('nightKey') === null) {
            this.showNightOffer();
          }
        }
      }

      this.$button.on('click', function (e) {
        e.preventDefault();

        if (localStorage.getItem('night') === 'true') {
          _this4.removeNight();
        } else {
          _this4.addNight();
        } // Запуск ночного режима в base.html

      });
      $('.js-modal-btn-day').on('click', function (e) {
        e.preventDefault();

        _this4.removeNight();
      });
    },
    addNight: function addNight() {
      this.$body.addClass('night');
      this.$button.removeClass('header__day').addClass('header__night');
      this.$button.html('День');
      localStorage.setItem('night', 'true');
    },
    removeNight: function removeNight() {
      this.$body.removeClass('night');
      this.$button.removeClass('header__night').addClass('header__day');
      this.$button.html('Ночь');
      localStorage.setItem('night', 'false');
    },
    showNightOffer: function showNightOffer() {
      this.addNight();
      $('.js-modal').filter('[data-modal="night"]').addClass('modal-show');
      sessionStorage.setItem('nightKey', 'true');
    }
  };
  NIGHT.init();
});
//# sourceMappingURL=base.js.map
