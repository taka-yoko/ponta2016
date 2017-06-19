Vue.component('gallery', {
  data(){
    return {
      tweet: {
        date: '2016/4/8',
        text: 'おりほー',
        image_url: 'http://pbs.twimg.com/media/CtrgugOVYAAFqC6.jpg'
      }
    }
  },
  template: `
    <div class="c-tweet">
      <div class="c-tweet-date">{{tweet.date}}</div>
      <div class="c-tweet-image">
        <img src={{tweet.image_url}} />
      </div>
      <p class="c-tweet-text">{{tweet.text}}</p>
    </div>
  `
})