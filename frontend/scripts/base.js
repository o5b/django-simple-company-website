$(() => {
	const BODY = {
		$body: $('body'),
		$menu: $('.js-menu'),
		$scroll: $('.js-menu-scroll'),
		$translator: $('.js-translator'),

		freeze() {
			const bodyWidth = this.$body.innerWidth();
			this.$body.addClass('body-freeze');
			this.$menu.css('marginRight', (this.$body.css('marginRight') ? '+=' : '') + (this.$body.innerWidth() - bodyWidth));
			this.$scroll.css('marginRight', (this.$body.css('marginRight') ? '+=' : '') + (this.$body.innerWidth() - bodyWidth));
			this.$translator.css('marginRight', (this.$body.css('marginRight') ? '+=' : '') + (this.$body.innerWidth() - bodyWidth));
			this.$body.css('marginRight', (this.$body.css('marginRight') ? '+=' : '') + (this.$body.innerWidth() - bodyWidth));
		},

		unfreeze() {
			const bodyWidth = this.$body.innerWidth();
			this.$body.removeClass('body-freeze');
			this.$menu.css('marginRight', `-=${(bodyWidth - this.$body.innerWidth())}`);
			this.$scroll.css('marginRight', `-=${(bodyWidth - this.$body.innerWidth())}`);
			this.$translator.css('marginRight', `-=${(bodyWidth - this.$body.innerWidth())}`);
			this.$body.css('marginRight', `-=${(bodyWidth - this.$body.innerWidth())}`);
		},
	};

	const MENU = {
		$menu: $('.js-menu'),

		init() {
			const $menuBtn = $('.js-menu-btn');
			$menuBtn.on('click', (e) => {
				e.preventDefault();
				this.$menu.addClass('menu-show');
				BODY.freeze();
			});

			const $menuClose = $('.js-menu-close');
			$menuClose.on('click', (e) => {
				e.preventDefault();
				this.$menu.removeClass('menu-show');
				setTimeout(() => {
					BODY.unfreeze();
				}, 500);
			});
		},
	};
	MENU.init();


	const MENUSCROLL = {
		menuScroll: $('.js-menu-scroll'),

		init() {
			window.addEventListener('scroll', this.menuScrollToggle.bind(this));
			this.menuScrollToggle();
		},

		menuScrollToggle() {
			if (window.pageYOffset > 200) {
				this.menuScroll.addClass('scroll-fixed');
			} else {
				this.menuScroll.removeClass('scroll-fixed');
			}
		},
	};
	MENUSCROLL.init();


	const MODAL = {
		init() {
			const $modalBtn = $('.js-modal-btn');
			$modalBtn.on('click', (e) => {
				e.preventDefault();
				const $this = $(e.currentTarget);
				const $modal = $('.js-modal').filter(`[data-modal="${$this.data('target')}"]`);
				$modal.addClass('modal-show');
				BODY.freeze();
			});

			const $modalClose = $('.js-modal-close');
			$modalClose.on('click', (e) => {
				e.preventDefault();
				$(e.currentTarget).closest('.js-modal').removeClass('modal-show');
				setTimeout(() => {
					BODY.unfreeze();
				}, 300);
			});
		},
	};
	MODAL.init();


	const SUBNAV = {
		subnav: $('.js-subnav-fixed'),
		subnavHeight: 0,
		anchor: $('.js-subnav-anchor'),
		link: undefined,
		sections: undefined,
		anchorTop: 0,
		anchorBottom: 0,
		generalOffset: 0,
		customGap: 90,

		init() {
			if (window.innerWidth <= 960) {
				window.addEventListener('scroll', this.subnavScrollToggle.bind(this));
				return;
			}

			this.subnav.fadeIn();

			if (!this.anchor.length) {
				return;
			}

			this.link = $('.js-subnav-link');
			this.sections = this.link.map((idx, el) => $(el.getAttribute('href')));

			setTimeout(() => {
				// Delay for correct calc height and offset
				this.anchorTop = this.anchor.offset().top;
				this.anchorBottom = this.anchorTop + this.anchor.height();
				this.subnavHeight = this.subnav.height();
				this.generalOffset = this.anchorTop;
				this.checkSubnav();

				window.addEventListener('scroll', this.checkSubnav.bind(this));
			}, 500);
		},

		checkSubnav() {
			const top = window.pageYOffset || document.documentElement.scrollTop;

			if (
				((this.anchorTop - top) < this.customGap) && ((top + this.subnavHeight) < this.anchorBottom)
			) {
				this.subnav.addClass('subnav-fixed');
				this.subnav.css('top', this.customGap);
			}

			if ((top + this.subnavHeight + this.customGap) > this.anchorBottom) {
				this.subnav.removeClass('subnav-fixed');
				this.subnav.css('top', (this.anchorBottom - this.subnavHeight - this.generalOffset));
			}

			if ((this.anchorTop - top) > this.customGap) {
				this.subnav.removeClass('subnav-fixed');
				this.subnav.css('top', 'auto');
			}

			this.sections.each((idx, el) => {
				if (el.offset().top > top) {
					this.link.removeClass('subnav__a-active');
					this.link.filter(`[href="#${el.attr('id')}"]`).addClass('subnav__a-active');
					return false;
				}

				return true;
			});
		},

		subnavScrollToggle() {
			if (window.pageYOffset > window.innerHeight) {
				this.subnav.addClass('subnav-fixed');
			} else {
				this.subnav.removeClass('subnav-fixed');
			}
		},
	};
	SUBNAV.init();


	const SMOOTHSCROLL = {
		init() {
			$('a[href*="#"]')
				.click((e) => {
					if (window.location.hostname === e.currentTarget.hostname) {
						let target = $(e.currentTarget.hash);
						target = target.length ? target : $(`[id=${e.currentTarget.hash.slice(1)}]`);
						if (target.length) {
							e.preventDefault();
							$('html, body').animate({
								scrollTop: target.offset().top - 80,
							}, 1000, () => {
								$(e.currentTarget).blur();
								return true;
							});
						}
					}
				});
		},
	};
	SMOOTHSCROLL.init();


	const SWIPER = {
		init() {
			$('.js-swiper').each((idx, el) => {
				const $swiper = $(el);
				const dataSwiper = $swiper.data('swiper') || {};
				const defaultParams = {
					direction: 'horizontal',
					slidesPerView: 4,
					spaceBetween: 0,
					roundLengths: true,
					loop: false,
					pagination: {
						el: $swiper.find('.js-swiper-pagination'),
						clickable: true,
						bulletClass: 'arrow__point',
						bulletActiveClass: 'arrow__point-active',
					},
					navigation: {
						prevEl: $swiper.find('.js-swiper-left'),
						nextEl: $swiper.find('.js-swiper-right'),
					},
					breakpoints: {
						// when window width is <= 320px
						320: {
							slidesPerView: 1,
							slidesPerGroup: 1,
						},
						// when window width is <= 576px
						576: {
							slidesPerView: 2,
							spaceBetween: 10,
						},
						// when window width is <= 992px
						992: {
							slidesPerView: 3,
						},
					},
					on: {
						init() {
							$swiper.find('.swiper-load').removeClass('swiper-load');
						},
					},
				};
				const params = Object.assign(defaultParams, dataSwiper);

				// eslint-disable-next-line
				new Swiper($swiper.find('.swiper-container'), params);
			});
		},
	};
	SWIPER.init();

	const PHOTO = {
		init() {
			$('.js-photo').jqPhotoSwipe({
				bgOpacity: 0.7,
			});

			$('.js-photo-content').find('a:has(img)').jqPhotoSwipe({
				bgOpacity: 0.7,
			});
		},
	};
	PHOTO.init();


	const APPOINTMENT = {
		init() {
			$('a[href="#appointment"]').on('click', () => {
				$('.js-modal-btn[data-target="appointment"]').trigger('click');
			});

			const $detail = $('.js-appointment-detail');

			$('.js-appointment-detail-btn').on('click', () => {
				$detail.slideToggle();
			});
		},
	};
	APPOINTMENT.init();


	const TIPPY = {
		init() {
			$('.js-tippy').each((idx, el) => {
				const html = document.querySelector(el.getAttribute('data-html')).innerHTML;
				tippy(el, {
					content: html,
					arrow: true,
					theme: 'light',
					arrowTransform: 'scale(2)',
					trigger: 'click',
				});
			});
		},
	};
	TIPPY.init();


	const FORM = {
		init() {
			const $form = $('.js-form');
			$form.on('submit', (e) => {
				e.preventDefault();
				const $this = $(e.currentTarget);
				const $submit = $this.find('[type="submit"]');
				const $successShow = $this.find('.js-form-success-show');
				const $successHide = $this.find('.js-form-success-hide');
				const data = new FormData($this.get(0));
				const submitText = $submit.text();

				$submit.text('Отправляю...');
				$submit.attr('disabled', 'disabled');

				$.ajax({
					url: $this.attr('action'),
					type: $this.attr('method'),
					data,
					cache: false,
					processData: false,
					contentType: false,
				}).done(() => {
					$successHide.slideUp();
					$successShow.slideDown();

					if ($this.data('goal')) {
						dataLayer.push({ event: $this.data('goal') });
					}
				}).fail((res) => {
					const message = Object
						.keys(res.responseJSON)
						.map(el => res.responseJSON[el])
						.join('\n');

					// eslint-disable-next-line
					window.alert(`Исправьте ошибки:\n ${message}`);
				}).always(() => {
					$submit.removeAttr('disabled');
					$submit.text(submitText);
				});

				return true;
			});
		},
	};
	FORM.init();


	const FLATPICKR = {
		init() {
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
				disable: [
					date => date.getDay() === 0,
				],
			});
		},
	};
	FLATPICKR.init();

	const HIGHLIGHT = {
		init() {
			const urlParams = new URLSearchParams(window.location.search);
			const highlight = urlParams.get('highlight');

			if (!highlight) {
				return false;
			}

			const $section = $('section');
			$section.mark(highlight, {
				done: () => {
					const $results = $section.find('mark');
					const $first = $results.first();
					if ($first.length) {
						setTimeout(() => {
							$('html, body').animate({
								scrollTop: $first.offset().top - 80,
							}, 500);
						}, 500);
					}
				},
			});
			return true;
		},
	};
	HIGHLIGHT.init();


	const NIGHT = {
		$button: $('.js-night-btn'),
		$body: $('body'),
		night_start: 20,
		night_end: 8,

		init() {
			const date = new Date();
			const hours = date.getHours();

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

			this.$button.on('click', (e) => {
				e.preventDefault();
				if (localStorage.getItem('night') === 'true') {
					this.removeNight();
				} else {
					this.addNight();
				}
				// Запуск ночного режима в base.html
			});

			$('.js-modal-btn-day').on('click', (e) => {
				e.preventDefault();
				this.removeNight();
			});
		},

		addNight() {
			this.$body.addClass('night');
			this.$button.removeClass('header__day').addClass('header__night');
			this.$button.html('День');
			localStorage.setItem('night', 'true');
		},

		removeNight() {
			this.$body.removeClass('night');
			this.$button.removeClass('header__night').addClass('header__day');
			this.$button.html('Ночь');
			localStorage.setItem('night', 'false');
		},

		showNightOffer() {
			this.addNight();
			$('.js-modal').filter('[data-modal="night"]').addClass('modal-show');
			sessionStorage.setItem('nightKey', 'true');
		},
	};
	NIGHT.init();
});
