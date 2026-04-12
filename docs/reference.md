# API reference

All **1010** endpoints across **52** resources, generated from `spec/openapi.json` (V5.3.2).

Method names match the OpenAPI path basename verbatim. Parameter names match the OpenAPI parameter names verbatim. See [naming rules](index.md#naming-rules).

## Resources

- [`client.bilibili_app`](#clientbilibiliapp) — `BilibiliApp`, 11 endpoints
- [`client.bilibili_web`](#clientbilibiliweb) — `BilibiliWeb`, 30 endpoints
- [`client.demo`](#clientdemo) — `Demo`, 9 endpoints
- [`client.douyin_app_v3`](#clientdouyinappv3) — `DouyinAppV3`, 47 endpoints
- [`client.douyin_billboard`](#clientdouyinbillboard) — `DouyinBillboard`, 31 endpoints
- [`client.douyin_creator`](#clientdouyincreator) — `DouyinCreator`, 16 endpoints
- [`client.douyin_creator_v2`](#clientdouyincreatorv2) — `DouyinCreatorV2`, 14 endpoints
- [`client.douyin_search`](#clientdouyinsearch) — `DouyinSearch`, 19 endpoints
- [`client.douyin_web`](#clientdouyinweb) — `DouyinWeb`, 76 endpoints
- [`client.douyin_xingtu`](#clientdouyinxingtu) — `DouyinXingtu`, 22 endpoints
- [`client.douyin_xingtu_v2`](#clientdouyinxingtuv2) — `DouyinXingtuV2`, 21 endpoints
- [`client.health_check`](#clienthealthcheck) — `HealthCheck`, 1 endpoints
- [`client.hybrid_parsing`](#clienthybridparsing) — `HybridParsing`, 1 endpoints
- [`client.instagram_v1`](#clientinstagramv1) — `InstagramV1`, 29 endpoints
- [`client.instagram_v2`](#clientinstagramv2) — `InstagramV2`, 27 endpoints
- [`client.instagram_v3`](#clientinstagramv3) — `InstagramV3`, 32 endpoints
- [`client.ios_shortcut`](#clientiosshortcut) — `IosShortcut`, 1 endpoints
- [`client.kuaishou_app`](#clientkuaishouapp) — `KuaishouApp`, 20 endpoints
- [`client.kuaishou_web`](#clientkuaishouweb) — `KuaishouWeb`, 13 endpoints
- [`client.lemon8_app`](#clientlemon8app) — `Lemon8App`, 16 endpoints
- [`client.linkedin_web`](#clientlinkedinweb) — `LinkedinWeb`, 25 endpoints
- [`client.pipixia_app`](#clientpipixiaapp) — `PipixiaApp`, 17 endpoints
- [`client.reddit_app`](#clientredditapp) — `RedditApp`, 24 endpoints
- [`client.sora2`](#clientsora2) — `Sora2`, 17 endpoints
- [`client.temp_mail`](#clienttempmail) — `TempMail`, 3 endpoints
- [`client.threads_web`](#clientthreadsweb) — `ThreadsWeb`, 11 endpoints
- [`client.tikhub_downloader`](#clienttikhubdownloader) — `TikhubDownloader`, 2 endpoints
- [`client.tikhub_user`](#clienttikhubuser) — `TikhubUser`, 6 endpoints
- [`client.tiktok_ads`](#clienttiktokads) — `TiktokAds`, 31 endpoints
- [`client.tiktok_analytics`](#clienttiktokanalytics) — `TiktokAnalytics`, 4 endpoints
- [`client.tiktok_app_v3`](#clienttiktokappv3) — `TiktokAppV3`, 75 endpoints
- [`client.tiktok_creator`](#clienttiktokcreator) — `TiktokCreator`, 14 endpoints
- [`client.tiktok_interaction`](#clienttiktokinteraction) — `TiktokInteraction`, 7 endpoints
- [`client.tiktok_shop_web`](#clienttiktokshopweb) — `TiktokShopWeb`, 15 endpoints
- [`client.tiktok_web`](#clienttiktokweb) — `TiktokWeb`, 59 endpoints
- [`client.toutiao_app`](#clienttoutiaoapp) — `ToutiaoApp`, 5 endpoints
- [`client.toutiao_web`](#clienttoutiaoweb) — `ToutiaoWeb`, 2 endpoints
- [`client.twitter_web`](#clienttwitterweb) — `TwitterWeb`, 13 endpoints
- [`client.wechat_channels`](#clientwechatchannels) — `WechatChannels`, 10 endpoints
- [`client.wechat_media_platform_web`](#clientwechatmediaplatformweb) — `WechatMediaPlatformWeb`, 10 endpoints
- [`client.weibo_app`](#clientweiboapp) — `WeiboApp`, 20 endpoints
- [`client.weibo_web`](#clientweiboweb) — `WeiboWeb`, 11 endpoints
- [`client.weibo_web_v2`](#clientweibowebv2) — `WeiboWebV2`, 33 endpoints
- [`client.xiaohongshu_app`](#clientxiaohongshuapp) — `XiaohongshuApp`, 12 endpoints
- [`client.xiaohongshu_app_v2`](#clientxiaohongshuappv2) — `XiaohongshuAppV2`, 21 endpoints
- [`client.xiaohongshu_web`](#clientxiaohongshuweb) — `XiaohongshuWeb`, 17 endpoints
- [`client.xiaohongshu_web_v2`](#clientxiaohongshuwebv2) — `XiaohongshuWebV2`, 18 endpoints
- [`client.xiaohongshu_web_v3`](#clientxiaohongshuwebv3) — `XiaohongshuWebV3`, 11 endpoints
- [`client.xigua_app_v2`](#clientxiguaappv2) — `XiguaAppV2`, 7 endpoints
- [`client.youtube_web`](#clientyoutubeweb) — `YoutubeWeb`, 21 endpoints
- [`client.youtube_web_v2`](#clientyoutubewebv2) — `YoutubeWebV2`, 19 endpoints
- [`client.zhihu_web`](#clientzhihuweb) — `ZhihuWeb`, 34 endpoints

---

## `client.bilibili_app`

**Class:** `tikhub.resources.bilibili_app.BilibiliApp` (sync) / `AsyncBilibiliApp` (async)

**Endpoints:** 11

| Method | Endpoint | Summary |
|---|---|---|
| `fetch_bangumi_tab()` | `GET /api/v1/bilibili/app/fetch_bangumi_tab` | 获取番剧推荐/Get bangumi tab |
| `fetch_cinema_tab()` | `GET /api/v1/bilibili/app/fetch_cinema_tab` | 获取影视推荐/Get cinema tab |
| `fetch_home_feed(idx=..., flush=..., pull=...)` | `GET /api/v1/bilibili/app/fetch_home_feed` | 获取主页推荐视频流/Get home feed |
| `fetch_one_video(av_id=..., bv_id=...)` | `GET /api/v1/bilibili/app/fetch_one_video` | 获取单个视频详情信息/Get single video data |
| `fetch_popular_feed(idx=..., last_param=...)` | `GET /api/v1/bilibili/app/fetch_popular_feed` | 获取热门推荐/Get popular feed |
| `fetch_reply_detail(root, av_id=..., bv_id=..., next_offset=..., ps=...)` | `GET /api/v1/bilibili/app/fetch_reply_detail` | 获取二级评论回复/Get reply detail |
| `fetch_search_all(keyword, page=..., page_size=..., order=...)` | `GET /api/v1/bilibili/app/fetch_search_all` | 综合搜索/search all |
| `fetch_search_by_type(keyword, search_type=..., page=..., page_size=..., order=...)` | `GET /api/v1/bilibili/app/fetch_search_by_type` | 分类搜索/ search by type |
| `fetch_user_info(user_id)` | `GET /api/v1/bilibili/app/fetch_user_info` | 获取用户信息/Get user info |
| `fetch_user_videos(user_id, post_filter=..., page=..., ps=...)` | `GET /api/v1/bilibili/app/fetch_user_videos` | 获取用户投稿视频/Get user videos |
| `fetch_video_comments(av_id=..., bv_id=..., mode=..., next_offset=...)` | `GET /api/v1/bilibili/app/fetch_video_comments` | 获取视频评论列表/Get video comments |

## `client.bilibili_web`

**Class:** `tikhub.resources.bilibili_web.BilibiliWeb` (sync) / `AsyncBilibiliWeb` (async)

**Endpoints:** 30

| Method | Endpoint | Summary |
|---|---|---|
| `bv_to_aid(bv_id)` | `GET /api/v1/bilibili/web/bv_to_aid` | 通过bv号获得视频aid号/Generate aid by bvid |
| `fetch_all_live_areas()` | `GET /api/v1/bilibili/web/fetch_all_live_areas` | 获取所有直播分区列表/Get a list of all live areas |
| `fetch_collect_folders(uid)` | `GET /api/v1/bilibili/web/fetch_collect_folders` | 获取用户所有收藏夹信息/Get user collection folders |
| `fetch_com_popular(pn=...)` | `GET /api/v1/bilibili/web/fetch_com_popular` | 获取综合热门视频信息/Get comprehensive popular video information |
| `fetch_comment_reply(bv_id, rpid, pn=...)` | `GET /api/v1/bilibili/web/fetch_comment_reply` | 获取视频下指定评论的回复/Get reply to the specified comment |
| `fetch_dynamic_detail(dynamic_id)` | `GET /api/v1/bilibili/web/fetch_dynamic_detail` | 获取动态详情/Get dynamic detail |
| `fetch_dynamic_detail_v2(dynamic_id)` | `GET /api/v1/bilibili/web/fetch_dynamic_detail_v2` | 获取动态详情v2/Get dynamic detail v2 |
| `fetch_general_search(keyword, order, page, page_size, duration=..., pubtime_begin_s=..., pubtime_end_s=...)` | `GET /api/v1/bilibili/web/fetch_general_search` | 获取综合搜索信息/Get general search data |
| `fetch_get_user_id(share_link)` | `GET /api/v1/bilibili/web/fetch_get_user_id` | 提取用户ID/Extract user ID |
| `fetch_hot_search(limit)` | `GET /api/v1/bilibili/web/fetch_hot_search` | 获取热门搜索信息/Get hot search data |
| `fetch_live_room_detail(room_id)` | `GET /api/v1/bilibili/web/fetch_live_room_detail` | 获取指定直播间信息/Get information of specified live room |
| `fetch_live_streamers(area_id, pn=...)` | `GET /api/v1/bilibili/web/fetch_live_streamers` | 获取指定分区正在直播的主播/Get live streamers of specified live area |
| `fetch_live_videos(room_id)` | `GET /api/v1/bilibili/web/fetch_live_videos` | 获取直播间视频流/Get live video data of specified room |
| `fetch_one_video(bv_id)` | `GET /api/v1/bilibili/web/fetch_one_video` | 获取单个视频详情信息/Get single video data |
| `fetch_one_video_v2(a_id, c_id)` | `GET /api/v1/bilibili/web/fetch_one_video_v2` | 获取单个视频详情信息V2/Get single video data V2 |
| `fetch_one_video_v3(url)` | `GET /api/v1/bilibili/web/fetch_one_video_v3` | 获取单个视频详情信息V3/Get single video data V3 |
| `fetch_user_collection_videos(folder_id, pn=...)` | `GET /api/v1/bilibili/web/fetch_user_collection_videos` | 获取指定收藏夹内视频数据/Gets video data from a collection folder |
| `fetch_user_dynamic(uid, offset=...)` | `GET /api/v1/bilibili/web/fetch_user_dynamic` | 获取指定用户动态/Get dynamic information of specified user |
| `fetch_user_post_videos(uid, pn=..., order=...)` | `GET /api/v1/bilibili/web/fetch_user_post_videos` | 获取用户主页作品数据/Get user homepage video data |
| `fetch_user_profile(uid)` | `GET /api/v1/bilibili/web/fetch_user_profile` | 获取指定用户的信息/Get information of specified user |
| `fetch_user_relation_stat(uid)` | `GET /api/v1/bilibili/web/fetch_user_relation_stat` | 获取用户关系状态统计/Get user relation stat (following and followers) |
| `fetch_user_up_stat(uid)` | `GET /api/v1/bilibili/web/fetch_user_up_stat` | 获取UP主状态统计/Get UP stat (total likes and views) |
| `fetch_video_comments(bv_id, pn=...)` | `GET /api/v1/bilibili/web/fetch_video_comments` | 获取指定视频的评论/Get comments on the specified video |
| `fetch_video_danmaku(cid)` | `GET /api/v1/bilibili/web/fetch_video_danmaku` | 获取视频实时弹幕/Get Video Danmaku |
| `fetch_video_detail(aid)` | `GET /api/v1/bilibili/web/fetch_video_detail` | 获取单个视频详情/Get single video detail |
| `fetch_video_parts(bv_id)` | `GET /api/v1/bilibili/web/fetch_video_parts` | 通过bv号获得视频分p信息/Get Video Parts By bvid |
| `fetch_video_play_info(url)` | `GET /api/v1/bilibili/web/fetch_video_play_info` | 获取单个视频播放信息/Get single video play info |
| `fetch_video_playurl(bv_id, cid)` | `GET /api/v1/bilibili/web/fetch_video_playurl` | 获取视频流地址/Get video playurl |
| `fetch_video_subtitle(a_id, c_id)` | `GET /api/v1/bilibili/web/fetch_video_subtitle` | 获取视频字幕信息/Get video subtitle info |
| `fetch_vip_video_playurl(bv_id, cid, cookie)` | `POST /api/v1/bilibili/web/fetch_vip_video_playurl` | 获取大会员清晰度视频流地址/Get VIP video playurl |

## `client.demo`

**Class:** `tikhub.resources.demo.Demo` (sync) / `AsyncDemo` (async)

**Endpoints:** 9

| Method | Endpoint | Summary |
|---|---|---|
| `article_extract()` | `GET /api/v1/demo/wechat/article_extract` | 【Demo】微信公众号文章提取（1小时缓存）/[Demo] WeChat Article Extract with Cache |
| `cache_status()` | `GET /api/v1/demo/demo/cache_status` | 查看Demo缓存状态/View Demo Cache Status |
| `douyin_app_fetch_one_video()` | `GET /api/v1/demo/douyin/app/fetch_one_video` | 【Demo】抖音APP获取固定作品数据（1小时缓存）/[Demo] Fetch Douyin APP Fixed Video Data with Cache |
| `douyin_web_fetch_one_video()` | `GET /api/v1/demo/douyin/web/fetch_one_video` | 【Demo】抖音Web获取固定作品数据（1小时缓存）/[Demo] Fetch Douyin Web Fixed Video Data with Cache |
| `fetch_user_info()` | `GET /api/v1/demo/instagram/web/fetch_user_info` | 【Demo】Instagram获取固定用户信息（1小时缓存）/[Demo] Instagram Fixed User Profile with Cache |
| `fetch_user_profile()` | `GET /api/v1/demo/tiktok/web/fetch_user_profile` | 【Demo】TikTok固定用户信息（1小时缓存）/[Demo] TikTok Fixed User Profile with Cache |
| `general_search()` | `GET /api/v1/demo/douyin_search/app/general_search` | 【Demo】抖音搜索综合搜索（1小时缓存）/[Demo] Douyin General Search with Cache |
| `kuaishou_web_fetch_one_video()` | `GET /api/v1/demo/kuaishou/web/fetch_one_video` | 【Demo】快手获取固定视频信息（1小时缓存）/[Demo] Kuaishou Fixed Video with Cache |
| `tiktok_app_fetch_one_video()` | `GET /api/v1/demo/tiktok/app/fetch_one_video` | 【Demo】TikTok APP获取固定视频详情（1小时缓存）/[Demo] TikTok APP Fixed Video Detail with Cache |

## `client.douyin_app_v3`

**Class:** `tikhub.resources.douyin_app_v3.DouyinAppV3` (sync) / `AsyncDouyinAppV3` (async)

**Endpoints:** 47

| Method | Endpoint | Summary |
|---|---|---|
| `add_video_play_count(aweme_type, item_id, cookie=...)` | `GET /api/v1/douyin/app/v3/add_video_play_count` | 根据视频ID来增加作品的播放数/Increase the number of plays of the work according to the video ID |
| `fetch_brand_hot_search_list()` | `GET /api/v1/douyin/app/v3/fetch_brand_hot_search_list` | 获取抖音品牌热榜分类数据/Get Douyin brand hot search list data |
| `fetch_brand_hot_search_list_detail(category_id)` | `GET /api/v1/douyin/app/v3/fetch_brand_hot_search_list_detail` | 获取抖音品牌热榜具体分类数据/Get Douyin brand hot search list detail data |
| `fetch_general_search_result(keyword, offset=..., count=..., sort_type=..., publish_time=..., filter_duration=..., content_type=...)` | `GET /api/v1/douyin/app/v3/fetch_general_search_result` | 获取指定关键词的综合搜索结果（弃用，替代接口见下方文档说明）/Get comprehensive search results of specified keywords (deprecated, see the documentation |
| `fetch_hashtag_detail(ch_id)` | `GET /api/v1/douyin/app/v3/fetch_hashtag_detail` | 获取指定话题的详情数据/Get details of specified hashtag |
| `fetch_hashtag_search_result(keyword, offset=..., count=...)` | `GET /api/v1/douyin/app/v3/fetch_hashtag_search_result` | 获取指定关键词的话题搜索结果（弃用，替代接口见下方文档说明）/Get hashtag search results of specified keywords (deprecated, see the documentation below |
| `fetch_hashtag_video_list(ch_id, cursor=..., sort_type=..., count=...)` | `GET /api/v1/douyin/app/v3/fetch_hashtag_video_list` | 获取指定话题的作品数据/Get video list of specified hashtag |
| `fetch_hot_search_list(board_type=..., board_sub_type=...)` | `GET /api/v1/douyin/app/v3/fetch_hot_search_list` | 获取抖音热搜榜数据/Get Douyin hot search list data |
| `fetch_live_hot_search_list()` | `GET /api/v1/douyin/app/v3/fetch_live_hot_search_list` | 获取抖音直播热搜榜数据/Get Douyin live hot search list data |
| `fetch_live_search_result(keyword, cursor=..., count=...)` | `GET /api/v1/douyin/app/v3/fetch_live_search_result` | 获取指定关键词的直播搜索结果（弃用，替代接口见下方文档说明）/Get live search results of specified keywords (deprecated, see the documentation below fo |
| `fetch_multi_video(body)` | `POST /api/v1/douyin/app/v3/fetch_multi_video` | 批量获取视频信息 V1/Batch Get Video Information V1 |
| `fetch_multi_video_high_quality_play_url(aweme_ids=...)` | `POST /api/v1/douyin/app/v3/fetch_multi_video_high_quality_play_url` | 批量获取视频的最高画质播放链接/Batch get the highest quality play URL of videos |
| `fetch_multi_video_statistics(aweme_ids)` | `GET /api/v1/douyin/app/v3/fetch_multi_video_statistics` | 根据视频ID批量获取作品的统计数据（点赞数、下载数、播放数、分享数）/Get the statistical data of the Post according to the video ID (like count, download  |
| `fetch_multi_video_v2(body)` | `POST /api/v1/douyin/app/v3/fetch_multi_video_v2` | 批量获取视频信息 V2/Batch Get Video Information V2 |
| `fetch_music_detail(music_id)` | `GET /api/v1/douyin/app/v3/fetch_music_detail` | 获取指定音乐的详情数据/Get details of specified music |
| `fetch_music_hot_search_list(chart_type=..., cursor=...)` | `GET /api/v1/douyin/app/v3/fetch_music_hot_search_list` | 获取抖音音乐榜数据/Get Douyin music hot search list data |
| `fetch_music_search_result(keyword, offset=..., count=...)` | `GET /api/v1/douyin/app/v3/fetch_music_search_result` | 获取指定关键词的音乐搜索结果（弃用，替代接口见下方文档说明）/Get music search results of specified keywords (deprecated, see the documentation below f |
| `fetch_music_video_list(music_id, cursor=..., count=...)` | `GET /api/v1/douyin/app/v3/fetch_music_video_list` | 获取指定音乐的视频列表数据/Get video list of specified music |
| `fetch_one_video(aweme_id)` | `GET /api/v1/douyin/app/v3/fetch_one_video` | 获取单个作品数据/Get single video data |
| `fetch_one_video_by_share_url(share_url)` | `GET /api/v1/douyin/app/v3/fetch_one_video_by_share_url` | 根据分享链接获取单个作品数据/Get single video data by sharing link |
| `fetch_one_video_v2(aweme_id)` | `GET /api/v1/douyin/app/v3/fetch_one_video_v2` | 获取单个作品数据 V2/Get single video data V2 |
| `fetch_one_video_v3(aweme_id)` | `GET /api/v1/douyin/app/v3/fetch_one_video_v3` | 获取单个作品数据 V3 (无版权限制)/Get single video data V3 (No copyright restrictions) |
| `fetch_series_detail(series_id)` | `GET /api/v1/douyin/app/v3/fetch_series_detail` | 获取短剧详情信息/Get series detail |
| `fetch_series_video_list(series_id, cursor=...)` | `GET /api/v1/douyin/app/v3/fetch_series_video_list` | 获取短剧视频列表/Get series video list |
| `fetch_share_info_by_share_code(share_code)` | `GET /api/v1/douyin/app/v3/fetch_share_info_by_share_code` | 根据分享口令获取分享信息/Get share info by share code |
| `fetch_user_fans_list(sec_user_id=..., max_time=..., count=...)` | `GET /api/v1/douyin/app/v3/fetch_user_fans_list` | 获取用户粉丝列表/Get user fans list |
| `fetch_user_following_list(sec_user_id=..., max_time=..., count=...)` | `GET /api/v1/douyin/app/v3/fetch_user_following_list` | 获取用户关注列表 (弃用，使用 /api/v1/douyin/web/fetch_user_following_list 替代)/Get user following list (Deprecated, use /api/v1/douyin |
| `fetch_user_like_videos(sec_user_id, max_cursor=..., counts=...)` | `GET /api/v1/douyin/app/v3/fetch_user_like_videos` | 获取用户喜欢作品数据/Get user like video data |
| `fetch_user_post_videos(sec_user_id, max_cursor=..., count=..., sort_type=...)` | `GET /api/v1/douyin/app/v3/fetch_user_post_videos` | 获取用户主页作品数据/Get user homepage video data |
| `fetch_user_search_result(keyword, offset=..., count=..., douyin_user_fans=..., douyin_user_type=...)` | `GET /api/v1/douyin/app/v3/fetch_user_search_result` | 获取指定关键词的用户搜索结果（弃用，替代接口见下方文档说明）/Get user search results of specified keywords (deprecated, see the documentation below fo |
| `fetch_user_series_list(user_id=..., sec_user_id=..., cursor=...)` | `GET /api/v1/douyin/app/v3/fetch_user_series_list` | 获取用户短剧合集列表/Get user series list |
| `fetch_video_comment_replies(item_id, comment_id, cursor=..., count=...)` | `GET /api/v1/douyin/app/v3/fetch_video_comment_replies` | 获取指定视频的评论回复数据/Get comment replies data of specified video |
| `fetch_video_comments(aweme_id, cursor=..., count=...)` | `GET /api/v1/douyin/app/v3/fetch_video_comments` | 获取单个视频评论数据/Get single video comments data |
| `fetch_video_high_quality_play_url(aweme_id=..., share_url=...)` | `GET /api/v1/douyin/app/v3/fetch_video_high_quality_play_url` | 获取视频的最高画质播放链接/Get the highest quality play URL of the video |
| `fetch_video_mix_detail(mix_id)` | `GET /api/v1/douyin/app/v3/fetch_video_mix_detail` | 获取抖音视频合集详情数据/Get Douyin video mix detail data |
| `fetch_video_mix_post_list(mix_id, cursor=..., count=...)` | `GET /api/v1/douyin/app/v3/fetch_video_mix_post_list` | 获取抖音视频合集作品列表数据/Get Douyin video mix post list data |
| `fetch_video_search_result(keyword, offset=..., count=..., sort_type=..., publish_time=..., filter_duration=...)` | `GET /api/v1/douyin/app/v3/fetch_video_search_result` | 获取指定关键词的视频搜索结果（弃用，替代接口见下方文档说明）/Get video search results of specified keywords (deprecated, see the documentation below f |
| `fetch_video_search_result_v2(keyword, sort_type=..., publish_time=..., filter_duration=..., page=..., search_id=...)` | `GET /api/v1/douyin/app/v3/fetch_video_search_result_v2` | 获取指定关键词的视频搜索结果 V2 （弃用，替代接口见下方文档说明）/Get video search results of specified keywords V2 (deprecated, see the documentation  |
| `fetch_video_statistics(aweme_ids)` | `GET /api/v1/douyin/app/v3/fetch_video_statistics` | 根据视频ID获取作品的统计数据（点赞数、下载数、播放数、分享数）/Get the statistical data of the Post according to the video ID (like count, download co |
| `generate_douyin_short_url(url)` | `GET /api/v1/douyin/app/v3/generate_douyin_short_url` | 生成抖音短链接/Generate Douyin short link |
| `generate_douyin_video_share_qrcode(object_id)` | `GET /api/v1/douyin/app/v3/generate_douyin_video_share_qrcode` | 生成抖音视频分享二维码/Generate Douyin video share QR code |
| `handler_user_profile(sec_user_id)` | `GET /api/v1/douyin/app/v3/handler_user_profile` | 获取指定用户的信息/Get information of specified user |
| `open_douyin_app_to_keyword_search(keyword)` | `GET /api/v1/douyin/app/v3/open_douyin_app_to_keyword_search` | 生成抖音分享链接，唤起抖音APP，跳转指定关键词搜索结果/Generate Douyin share link, call Douyin APP, and jump to the specified keyword search resul |
| `open_douyin_app_to_send_private_message(uid, sec_uid)` | `GET /api/v1/douyin/app/v3/open_douyin_app_to_send_private_message` | 生成抖音分享链接，唤起抖音APP，给指定用户发送私信/Generate Douyin share link, call Douyin APP, and send private messages to specified users |
| `open_douyin_app_to_user_profile(uid, sec_uid)` | `GET /api/v1/douyin/app/v3/open_douyin_app_to_user_profile` | 生成抖音分享链接，唤起抖音APP，跳转指定用户主页/Generate Douyin share link, call Douyin APP, and jump to the specified user profile |
| `open_douyin_app_to_video_detail(aweme_id)` | `GET /api/v1/douyin/app/v3/open_douyin_app_to_video_detail` | 生成抖音分享链接，唤起抖音APP，跳转指定作品详情页/Generate Douyin share link, call Douyin APP, and jump to the specified video details page |
| `register_device(proxy=...)` | `GET /api/v1/douyin/app/v3/register_device` | 抖音APP注册设备/Douyin APP register device |

## `client.douyin_billboard`

**Class:** `tikhub.resources.douyin_billboard.DouyinBillboard` (sync) / `AsyncDouyinBillboard` (async)

**Endpoints:** 31

| Method | Endpoint | Summary |
|---|---|---|
| `fetch_city_list()` | `GET /api/v1/douyin/billboard/fetch_city_list` | 获取中国城市列表/Fetch Chinese city list |
| `fetch_content_tag()` | `GET /api/v1/douyin/billboard/fetch_content_tag` | 获取垂类内容标签/Fetch vertical content tags |
| `fetch_hot_account_fans_interest_account_list(sec_uid)` | `GET /api/v1/douyin/billboard/fetch_hot_account_fans_interest_account_list` | 获取粉丝兴趣作者 20个用户/Fetch fan interest author 20 users |
| `fetch_hot_account_fans_interest_search_list(sec_uid)` | `GET /api/v1/douyin/billboard/fetch_hot_account_fans_interest_search_list` | 获取粉丝近3天搜索词 10个搜索词/Fetch fan interest search term in the last 3 days 10 search terms |
| `fetch_hot_account_fans_interest_topic_list(sec_uid)` | `GET /api/v1/douyin/billboard/fetch_hot_account_fans_interest_topic_list` | 获取粉丝近3天感兴趣的话题 10个话题/Fetch fan interest topic in the last 3 days 10 topics |
| `fetch_hot_account_fans_portrait_list(sec_uid, option=...)` | `GET /api/v1/douyin/billboard/fetch_hot_account_fans_portrait_list` | 获取粉丝画像/Fetch fan portrait |
| `fetch_hot_account_item_analysis_list(sec_uid)` | `GET /api/v1/douyin/billboard/fetch_hot_account_item_analysis_list` | 获取账号作品分析-上周/Fetch account work analysis - last week |
| `fetch_hot_account_list(date_window=..., page_num=..., page_size=..., query_tag=...)` | `POST /api/v1/douyin/billboard/fetch_hot_account_list` | 获取热门账号/Fetch hot account list |
| `fetch_hot_account_search_list(keyword, cursor)` | `GET /api/v1/douyin/billboard/fetch_hot_account_search_list` | 搜索用户名或抖音号/Fetch account search list |
| `fetch_hot_account_trends_list(sec_uid, option=..., date_window=...)` | `GET /api/v1/douyin/billboard/fetch_hot_account_trends_list` | 获取账号粉丝数据趋势/Fetch account fan data trend |
| `fetch_hot_calendar_detail(calendar_id)` | `GET /api/v1/douyin/billboard/fetch_hot_calendar_detail` | 获取活动日历详情/Fetch activity calendar detail |
| `fetch_hot_calendar_list(city_code=..., category_code=..., end_date=..., start_date=...)` | `POST /api/v1/douyin/billboard/fetch_hot_calendar_list` | 获取活动日历/Fetch activity calendar |
| `fetch_hot_category_list(billboard_type, snapshot_time=..., start_date=..., end_date=..., keyword=...)` | `GET /api/v1/douyin/billboard/fetch_hot_category_list` | 获取热点榜分类/Fetch hot list category |
| `fetch_hot_challenge_list(page, page_size, keyword=...)` | `GET /api/v1/douyin/billboard/fetch_hot_challenge_list` | 获取挑战热榜/Fetch hot challenge list |
| `fetch_hot_city_list(page, page_size, order, city_code=..., sentence_tag=..., keyword=...)` | `GET /api/v1/douyin/billboard/fetch_hot_city_list` | 获取同城热点榜/Fetch city hot list |
| `fetch_hot_comment_word_list(aweme_id)` | `GET /api/v1/douyin/billboard/fetch_hot_comment_word_list` | 获取作品评论分析-词云权重/Fetch work comment analysis word cloud weight |
| `fetch_hot_item_trends_list(aweme_id=..., option=..., date_window=...)` | `GET /api/v1/douyin/billboard/fetch_hot_item_trends_list` | 获取作品数据趋势/Fetch post data trend |
| `fetch_hot_rise_list(page, page_size, order, sentence_tag=..., keyword=...)` | `GET /api/v1/douyin/billboard/fetch_hot_rise_list` | 获取上升热点榜/Fetch rising hot list |
| `fetch_hot_total_high_fan_list(page=..., page_size=..., date_window=..., tags=...)` | `POST /api/v1/douyin/billboard/fetch_hot_total_high_fan_list` | 获取高涨粉率榜/Fetch high fan rate list |
| `fetch_hot_total_high_like_list(page=..., page_size=..., date_window=..., tags=...)` | `POST /api/v1/douyin/billboard/fetch_hot_total_high_like_list` | 获取高点赞率榜/Fetch high like rate list |
| `fetch_hot_total_high_play_list(page=..., page_size=..., date_window=..., tags=...)` | `POST /api/v1/douyin/billboard/fetch_hot_total_high_play_list` | 获取高完播率榜/Fetch high completion rate list |
| `fetch_hot_total_high_search_list(page_num=..., page_size=..., date_window=..., keyword=...)` | `POST /api/v1/douyin/billboard/fetch_hot_total_high_search_list` | 获取热度飙升的搜索榜/Fetch search list with rising popularity |
| `fetch_hot_total_high_topic_list(page=..., page_size=..., date_window=..., tags=...)` | `POST /api/v1/douyin/billboard/fetch_hot_total_high_topic_list` | 获取热度飙升的话题榜/Fetch topic list with rising popularity |
| `fetch_hot_total_hot_word_detail_list(keyword, word_id, query_day)` | `GET /api/v1/douyin/billboard/fetch_hot_total_hot_word_detail_list` | 获取内容词详情/Fetch content word details |
| `fetch_hot_total_hot_word_list(page_num=..., page_size=..., date_window=..., keyword=...)` | `POST /api/v1/douyin/billboard/fetch_hot_total_hot_word_list` | 获取全部热门内容词/Fetch all hot content words |
| `fetch_hot_total_list(page, page_size, type, snapshot_time=..., start_date=..., end_date=..., sentence_tag=..., keyword=...)` | `GET /api/v1/douyin/billboard/fetch_hot_total_list` | 获取热点总榜/Fetch total hot list |
| `fetch_hot_total_low_fan_list(page=..., page_size=..., date_window=..., tags=...)` | `POST /api/v1/douyin/billboard/fetch_hot_total_low_fan_list` | 获取低粉爆款榜/Fetch low fan explosion list |
| `fetch_hot_total_search_list(page_num=..., page_size=..., date_window=..., keyword=...)` | `POST /api/v1/douyin/billboard/fetch_hot_total_search_list` | 获取搜索热榜/Fetch search hot list |
| `fetch_hot_total_topic_list(page=..., page_size=..., date_window=..., tags=...)` | `POST /api/v1/douyin/billboard/fetch_hot_total_topic_list` | 获取话题热榜/Fetch topic hot list |
| `fetch_hot_total_video_list(page=..., page_size=..., date_window=..., sub_type=..., tags=...)` | `POST /api/v1/douyin/billboard/fetch_hot_total_video_list` | 获取视频热榜/Fetch video hot list |
| `fetch_hot_user_portrait_list(aweme_id, option=...)` | `GET /api/v1/douyin/billboard/fetch_hot_user_portrait_list` | 获取作品点赞观众画像-仅限热门榜/Fetch work like audience portrait - hot list only |

## `client.douyin_creator`

**Class:** `tikhub.resources.douyin_creator.DouyinCreator` (sync) / `AsyncDouyinCreator` (async)

**Endpoints:** 16

| Method | Endpoint | Summary |
|---|---|---|
| `fetch_creator_activity_detail(activity_id)` | `GET /api/v1/douyin/creator/fetch_creator_activity_detail` | 获取创作者活动详情/Get creator activity detail |
| `fetch_creator_activity_list(start_time, end_time)` | `GET /api/v1/douyin/creator/fetch_creator_activity_list` | 获取创作者活动列表/Get creator activity list |
| `fetch_creator_content_category()` | `GET /api/v1/douyin/creator/fetch_creator_content_category` | 获取创作者内容创作合集分类/Get creator content creation category |
| `fetch_creator_content_course(category_id, order=..., limit=..., offset=...)` | `GET /api/v1/douyin/creator/fetch_creator_content_course` | 获取创作者内容创作课程/Get creator content creation course |
| `fetch_creator_hot_challenge_billboard()` | `GET /api/v1/douyin/creator/fetch_creator_hot_challenge_billboard` | 获取创作者热门挑战榜单/Get creator hot challenge billboard |
| `fetch_creator_hot_course(order=..., limit=..., offset=..., category_id=...)` | `GET /api/v1/douyin/creator/fetch_creator_hot_course` | 获取创作者热门课程/Get creator hot course |
| `fetch_creator_hot_music_billboard(billboard_tag=..., order_key=..., time_filter=...)` | `GET /api/v1/douyin/creator/fetch_creator_hot_music_billboard` | 获取创作者热门音乐榜单/Get creator hot music billboard |
| `fetch_creator_hot_props_billboard(billboard_tag=..., order_key=..., time_filter=...)` | `GET /api/v1/douyin/creator/fetch_creator_hot_props_billboard` | 获取创作者热门道具榜单/Get creator hot props billboard |
| `fetch_creator_hot_spot_billboard(billboard_tag=..., hot_search_type=..., city_code=...)` | `GET /api/v1/douyin/creator/fetch_creator_hot_spot_billboard` | 获取创作者中心创作热点/Get creator hot spot billboard |
| `fetch_creator_hot_topic_billboard(billboard_tag=..., order_key=..., time_filter=...)` | `GET /api/v1/douyin/creator/fetch_creator_hot_topic_billboard` | 获取创作者热门话题榜单/Get creator hot topic billboard |
| `fetch_creator_material_center_billboard(billboard_tag=..., order_key=..., time_filter=...)` | `GET /api/v1/douyin/creator/fetch_creator_material_center_billboard` | 获取创作者中心热门视频榜单/Get creator material center billboard |
| `fetch_creator_material_center_config()` | `GET /api/v1/douyin/creator/fetch_creator_material_center_config` | 获取创作者中心配置/Get creator material center config |
| `fetch_industry_category_config()` | `GET /api/v1/douyin/creator/fetch_industry_category_config` | 获取行业分类配置/Get industry category config |
| `fetch_mission_task_list(cursor=..., limit=..., mission_type=..., tab_scene=..., industry_lv1=..., industry_lv2=..., platform_channel=..., pay_type=..., greater_than_cost_progress=..., publish_time_start=..., quick_selector_scene=..., keyword=...)` | `GET /api/v1/douyin/creator/fetch_mission_task_list` | 获取商单任务列表/Get mission task list |
| `fetch_user_search(user_name)` | `GET /api/v1/douyin/creator/fetch_user_search` | 搜索用户/Search users |
| `fetch_video_danmaku_list(item_id, count=..., offset=..., order_type=..., is_blocked=...)` | `GET /api/v1/douyin/creator/fetch_video_danmaku_list` | 获取作品弹幕列表/Get video danmaku list |

## `client.douyin_creator_v2`

**Class:** `tikhub.resources.douyin_creator_v2.DouyinCreatorV2` (sync) / `AsyncDouyinCreatorV2` (async)

**Endpoints:** 14

| Method | Endpoint | Summary |
|---|---|---|
| `fetch_author_diagnosis(cookie)` | `POST /api/v1/douyin/creator_v2/fetch_author_diagnosis` | 获取创作者账号诊断/Fetch author diagnosis |
| `fetch_item_analysis_involved_vertical(cookie, start_date, end_date)` | `POST /api/v1/douyin/creator_v2/fetch_item_analysis_involved_vertical` | 获取作品垂类标签/Fetch item analysis involved vertical |
| `fetch_item_analysis_item_performance(cookie, start_date, end_date, primary_verticals, genres=..., metric_type=...)` | `POST /api/v1/douyin/creator_v2/fetch_item_analysis_item_performance` | 获取投稿表现数据/Fetch item analysis item performance |
| `fetch_item_analysis_overview(cookie, start_date, end_date, primary_verticals, genres=...)` | `POST /api/v1/douyin/creator_v2/fetch_item_analysis_overview` | 获取投稿分析概览/Fetch item analysis overview |
| `fetch_item_audience_others(cookie, item_id)` | `POST /api/v1/douyin/creator_v2/fetch_item_audience_others` | 获取作品观众其他数据分析/Fetch item audience others analysis |
| `fetch_item_audience_portrait(cookie, item_id)` | `POST /api/v1/douyin/creator_v2/fetch_item_audience_portrait` | 获取作品观众数据分析/Fetch item audience portrait |
| `fetch_item_danmaku_analysis(cookie, item_id)` | `POST /api/v1/douyin/creator_v2/fetch_item_danmaku_analysis` | 获取作品弹幕分析/Fetch item bullet analysis |
| `fetch_item_list(cookie, start_time, end_time, count=..., order_by=..., fields=..., need_cooperation=..., need_long_article=..., cursor=...)` | `POST /api/v1/douyin/creator_v2/fetch_item_list` | 获取投稿作品列表/Fetch item list |
| `fetch_item_list_download(cookie, min_cursor, max_cursor, type_filters=..., need_long_article=...)` | `POST /api/v1/douyin/creator_v2/fetch_item_list_download` | 导出投稿作品列表/Download item list |
| `fetch_item_overview_data(cookie, ids, fields=...)` | `POST /api/v1/douyin/creator_v2/fetch_item_overview_data` | 获取作品总览数据/Fetch item overview data |
| `fetch_item_play_source(cookie, item_id)` | `POST /api/v1/douyin/creator_v2/fetch_item_play_source` | 获取作品流量来源统计/Fetch item play source statistics |
| `fetch_item_search_keyword(cookie, item_id)` | `POST /api/v1/douyin/creator_v2/fetch_item_search_keyword` | 获取作品搜索关键词统计/Fetch item search keywords statistics |
| `fetch_item_watch_trend(cookie, item_id, analysis_type=...)` | `POST /api/v1/douyin/creator_v2/fetch_item_watch_trend` | 获取作品观看趋势分析/Fetch item watch trend analysis |
| `fetch_live_room_history_list(cookie, start_date, end_date, limit=..., need_living=..., download=...)` | `POST /api/v1/douyin/creator_v2/fetch_live_room_history_list` | 获取直播场次历史记录/Fetch live room history list |

## `client.douyin_search`

**Class:** `tikhub.resources.douyin_search.DouyinSearch` (sync) / `AsyncDouyinSearch` (async)

**Endpoints:** 19

| Method | Endpoint | Summary |
|---|---|---|
| `fetch_challenge_search_v1(keyword=..., cursor=..., sort_type=..., publish_time=..., filter_duration=..., content_type=..., search_id=..., backtrace=...)` | `POST /api/v1/douyin/search/fetch_challenge_search_v1` | 获取话题搜索 V1/Fetch hashtag search V1 |
| `fetch_challenge_search_v2(keyword=..., cursor=..., sort_type=..., publish_time=..., filter_duration=..., content_type=..., search_id=..., backtrace=...)` | `POST /api/v1/douyin/search/fetch_challenge_search_v2` | 获取话题搜索 V2/Fetch hashtag search V2 |
| `fetch_challenge_suggest(keyword=...)` | `POST /api/v1/douyin/search/fetch_challenge_suggest` | 获取话题推荐搜索/Fetch hashtag suggestions |
| `fetch_discuss_search(keyword=..., cursor=..., sort_type=..., publish_time=..., filter_duration=..., content_type=..., search_id=..., backtrace=...)` | `POST /api/v1/douyin/search/fetch_discuss_search` | 获取讨论搜索/Fetch discussion search |
| `fetch_experience_search(keyword=..., cursor=..., sort_type=..., publish_time=..., filter_duration=..., content_type=..., search_id=..., backtrace=...)` | `POST /api/v1/douyin/search/fetch_experience_search` | 获取经验搜索/Fetch experience search |
| `fetch_general_search_v1(keyword=..., cursor=..., sort_type=..., publish_time=..., filter_duration=..., content_type=..., search_id=..., backtrace=...)` | `POST /api/v1/douyin/search/fetch_general_search_v1` | 获取综合搜索 V1/Fetch general search V1 |
| `fetch_general_search_v2(keyword=..., cursor=..., sort_type=..., publish_time=..., filter_duration=..., content_type=..., search_id=..., backtrace=...)` | `POST /api/v1/douyin/search/fetch_general_search_v2` | 获取综合搜索 V2/Fetch general search V2 |
| `fetch_image_search(keyword=..., cursor=..., sort_type=..., publish_time=..., filter_duration=..., content_type=..., search_id=..., backtrace=...)` | `POST /api/v1/douyin/search/fetch_image_search` | 获取图片搜索/Fetch image search |
| `fetch_image_search_v3(keyword, cursor=..., search_id=...)` | `POST /api/v1/douyin/search/fetch_image_search_v3` | 获取图文搜索 V3/Fetch image-text search V3 |
| `fetch_live_search_v1(keyword=..., cursor=..., sort_type=..., publish_time=..., filter_duration=..., content_type=..., search_id=..., backtrace=...)` | `POST /api/v1/douyin/search/fetch_live_search_v1` | 获取直播搜索 V1/Fetch live search V1 |
| `fetch_multi_search(keyword=..., cursor=..., sort_type=..., publish_time=..., filter_duration=..., content_type=..., search_id=..., backtrace=...)` | `POST /api/v1/douyin/search/fetch_multi_search` | 获取多重搜索/Fetch multi-type search |
| `fetch_music_search(keyword=..., cursor=..., sort_type=..., publish_time=..., filter_duration=..., content_type=..., search_id=..., backtrace=...)` | `POST /api/v1/douyin/search/fetch_music_search` | 获取音乐搜索/Fetch music search |
| `fetch_school_search(keyword=...)` | `POST /api/v1/douyin/search/fetch_school_search` | 获取学校搜索/Fetch school search |
| `fetch_search_suggest(keyword=...)` | `POST /api/v1/douyin/search/fetch_search_suggest` | 获取搜索关键词推荐/Fetch search keyword suggestions |
| `fetch_user_search(keyword=..., cursor=..., douyin_user_fans=..., douyin_user_type=..., search_id=...)` | `POST /api/v1/douyin/search/fetch_user_search` | 获取用户搜索/Fetch user search |
| `fetch_user_search_v2(keyword=..., cursor=...)` | `POST /api/v1/douyin/search/fetch_user_search_v2` | 获取用户搜索 V2/Fetch user search V2 |
| `fetch_video_search_v1(keyword=..., cursor=..., sort_type=..., publish_time=..., filter_duration=..., content_type=..., search_id=..., backtrace=...)` | `POST /api/v1/douyin/search/fetch_video_search_v1` | 获取视频搜索 V1/Fetch video search V1 |
| `fetch_video_search_v2(keyword=..., cursor=..., sort_type=..., publish_time=..., filter_duration=..., content_type=..., search_id=..., backtrace=...)` | `POST /api/v1/douyin/search/fetch_video_search_v2` | 获取视频搜索 V2/Fetch video search V2 |
| `fetch_vision_search(image_uri, cursor=..., search_id=..., search_source=..., detection=..., detection_index=..., user_query=..., aweme_id=...)` | `POST /api/v1/douyin/search/fetch_vision_search` | 获取图像识别搜索/Fetch vision search (image-based search) |

## `client.douyin_web`

**Class:** `tikhub.resources.douyin_web.DouyinWeb` (sync) / `AsyncDouyinWeb` (async)

**Endpoints:** 76

| Method | Endpoint | Summary |
|---|---|---|
| `douyin_live_room(live_room_url, danmaku_type)` | `GET /api/v1/douyin/web/douyin_live_room` | 提取直播间弹幕/Extract live room danmaku |
| `encrypt_uid_to_sec_user_id(uid)` | `GET /api/v1/douyin/web/encrypt_uid_to_sec_user_id` | 加密用户uid到sec_user_id/Encrypt user uid to sec_user_id |
| `fetch_batch_user_profile_v1(sec_user_ids)` | `GET /api/v1/douyin/web/fetch_batch_user_profile_v1` | 获取批量用户信息(最多10个)/Get batch user profile (up to 10) |
| `fetch_batch_user_profile_v2(sec_user_ids)` | `GET /api/v1/douyin/web/fetch_batch_user_profile_v2` | 获取批量用户信息(最多50个)/Get batch user profile (up to 50) |
| `fetch_cartoon_aweme(count, refresh_index=..., cookie=...)` | `GET /api/v1/douyin/web/fetch_cartoon_aweme` | 二次元作品推荐/Anime Video |
| `fetch_challenge_posts(challenge_id=..., sort_type=..., cursor=..., count=..., cookie=...)` | `POST /api/v1/douyin/web/fetch_challenge_posts` | 话题作品/Challenge Posts |
| `fetch_douyin_web_guest_cookie(user_agent)` | `GET /api/v1/douyin/web/fetch_douyin_web_guest_cookie` | 获取抖音Web的游客Cookie/Get the guest Cookie of Douyin Web |
| `fetch_food_aweme(count, refresh_index=..., cookie=...)` | `GET /api/v1/douyin/web/fetch_food_aweme` | 美食作品推荐/Food Video |
| `fetch_game_aweme(count, refresh_index=..., cookie=...)` | `GET /api/v1/douyin/web/fetch_game_aweme` | 游戏作品推荐/Game Video |
| `fetch_general_search_result(keyword, offset=..., count=..., sort_type=..., publish_time=..., filter_duration=..., search_range=..., content_type=..., search_id=...)` | `GET /api/v1/douyin/web/fetch_general_search_result` | [已弃用/Deprecated] 获取指定关键词的综合搜索结果/Get comprehensive search results of specified keywords |
| `fetch_home_feed(count=..., refresh_index=...)` | `GET /api/v1/douyin/web/fetch_home_feed` | 获取首页推荐数据/Get home feed data |
| `fetch_hot_search_result()` | `GET /api/v1/douyin/web/fetch_hot_search_result` | 获取抖音热榜数据/Get Douyin hot search results |
| `fetch_knowledge_aweme(count, refresh_index=..., cookie=...)` | `GET /api/v1/douyin/web/fetch_knowledge_aweme` | 知识作品推荐/Knowledge Video |
| `fetch_live_gift_ranking(room_id, rank_type=...)` | `GET /api/v1/douyin/web/fetch_live_gift_ranking` | 获取直播间送礼用户排行榜/Get live room gift user ranking |
| `fetch_live_im_fetch(room_id, user_unique_id)` | `GET /api/v1/douyin/web/fetch_live_im_fetch` | 抖音直播间弹幕参数获取/Douyin live room danmaku parameters |
| `fetch_live_room_product_result(room_id, author_id, offset=..., limit=...)` | `GET /api/v1/douyin/web/fetch_live_room_product_result` | 抖音直播间商品信息/Douyin live room product information |
| `fetch_live_search_result(keyword, offset=..., count=..., search_id=...)` | `GET /api/v1/douyin/web/fetch_live_search_result` | [已弃用/Deprecated] 获取指定关键词的直播搜索结果/Get live search results of specified keywords |
| `fetch_multi_video(body)` | `POST /api/v1/douyin/web/fetch_multi_video` | 批量获取视频信息/Batch Get Video Information |
| `fetch_multi_video_high_quality_play_url(aweme_ids=...)` | `POST /api/v1/douyin/web/fetch_multi_video_high_quality_play_url` | 批量获取视频的最高画质播放链接/Batch get the highest quality play URL of videos |
| `fetch_music_aweme(count, refresh_index=..., cookie=...)` | `GET /api/v1/douyin/web/fetch_music_aweme` | 音乐作品推荐/Music Video |
| `fetch_one_video(aweme_id, need_anchor_info=...)` | `GET /api/v1/douyin/web/fetch_one_video` | 获取单个作品数据/Get single video data |
| `fetch_one_video_by_share_url(share_url)` | `GET /api/v1/douyin/web/fetch_one_video_by_share_url` | 根据分享链接获取单个作品数据/Get single video data by sharing link |
| `fetch_one_video_danmaku(item_id, duration, end_time, start_time)` | `GET /api/v1/douyin/web/fetch_one_video_danmaku` | 获取单个作品视频弹幕数据/Get single video danmaku data |
| `fetch_one_video_v2(aweme_id)` | `GET /api/v1/douyin/web/fetch_one_video_v2` | 获取单个作品数据 V2/Get single video data V2 |
| `fetch_product_coupon(product_id, shop_id, price, author_id, sec_user_id)` | `GET /api/v1/douyin/web/fetch_product_coupon` | 获取商品优惠券信息/Get product coupon information |
| `fetch_product_detail(product_id, aweme_id=..., room_id=..., sec_user_id=...)` | `GET /api/v1/douyin/web/fetch_product_detail` | 获取商品详情/Get product detail |
| `fetch_product_review_list(product_id, shop_id, cursor=..., count=..., sort_type=...)` | `GET /api/v1/douyin/web/fetch_product_review_list` | 获取商品评价列表/Get product review list |
| `fetch_product_review_score(product_id, shop_id)` | `GET /api/v1/douyin/web/fetch_product_review_score` | 获取商品评价评分/Get product review score |
| `fetch_product_sku_list(product_id, author_id)` | `GET /api/v1/douyin/web/fetch_product_sku_list` | 获取商品SKU列表/Get product SKU list |
| `fetch_query_user(body=...)` | `POST /api/v1/douyin/web/fetch_query_user` | 查询抖音用户基本信息/Query Douyin user basic information |
| `fetch_related_posts(aweme_id, refresh_index=..., count=...)` | `GET /api/v1/douyin/web/fetch_related_posts` | 获取相关作品推荐数据/Get related posts recommendation data |
| `fetch_search_challenge(keyword=..., cursor=..., count=..., cookie=...)` | `POST /api/v1/douyin/web/fetch_search_challenge` | [已弃用/Deprecated] 搜索话题/Search Challenge |
| `fetch_series_aweme(offset, count, content_type, cookie=...)` | `GET /api/v1/douyin/web/fetch_series_aweme` | 短剧作品/Series Video |
| `fetch_user_collection_videos(cookie, max_cursor=..., counts=...)` | `POST /api/v1/douyin/web/fetch_user_collection_videos` | 获取用户收藏作品数据/Get user collection video data |
| `fetch_user_collects(cookie, max_cursor=..., counts=...)` | `POST /api/v1/douyin/web/fetch_user_collects` | 获取用户收藏夹/Get user collection |
| `fetch_user_collects_videos(collects_id, max_cursor=..., counts=...)` | `GET /api/v1/douyin/web/fetch_user_collects_videos` | 获取用户收藏夹数据/Get user collection data |
| `fetch_user_fans_list(sec_user_id=..., max_time=..., count=..., source_type=...)` | `GET /api/v1/douyin/web/fetch_user_fans_list` | 获取用户粉丝列表/Get user fans list |
| `fetch_user_following_list(sec_user_id=..., max_time=..., count=..., source_type=...)` | `GET /api/v1/douyin/web/fetch_user_following_list` | 获取用户关注列表/Get user following list |
| `fetch_user_like_videos(sec_user_id, max_cursor=..., counts=..., cookie=...)` | `POST /api/v1/douyin/web/fetch_user_like_videos` | 获取用户喜欢作品数据/Get user like video data |
| `fetch_user_live_info_by_uid(uid)` | `GET /api/v1/douyin/web/fetch_user_live_info_by_uid` | 使用UID获取用户开播信息/Get user live information by UID |
| `fetch_user_live_videos(webcast_id)` | `GET /api/v1/douyin/web/fetch_user_live_videos` | 获取用户直播流数据/Get user live video data |
| `fetch_user_live_videos_by_room_id(room_id)` | `GET /api/v1/douyin/web/fetch_user_live_videos_by_room_id` | 通过room_id获取指定用户的直播流数据 V1/Get live video data of specified user by room_id V1 |
| `fetch_user_live_videos_by_room_id_v2(room_id)` | `GET /api/v1/douyin/web/fetch_user_live_videos_by_room_id_v2` | 通过room_id获取指定用户的直播流数据 V2/Gets the live stream data of the specified user by room_id V2 |
| `fetch_user_live_videos_by_sec_uid(sec_uid)` | `GET /api/v1/douyin/web/fetch_user_live_videos_by_sec_uid` | 通过sec_uid获取指定用户的直播流数据/Get live video data of specified user by sec_uid |
| `fetch_user_mix_videos(mix_id, max_cursor=..., counts=...)` | `GET /api/v1/douyin/web/fetch_user_mix_videos` | 获取用户合辑作品数据/Get user mix video data |
| `fetch_user_post_videos(sec_user_id, max_cursor=..., count=..., filter_type=..., cookie=...)` | `GET /api/v1/douyin/web/fetch_user_post_videos` | 获取用户主页作品数据/Get user homepage video data |
| `fetch_user_profile_by_short_id(short_id)` | `GET /api/v1/douyin/web/fetch_user_profile_by_short_id` | 使用Short ID获取用户信息/Get user information by Short ID |
| `fetch_user_profile_by_uid(uid)` | `GET /api/v1/douyin/web/fetch_user_profile_by_uid` | 使用UID获取用户信息/Get user information by UID |
| `fetch_user_search_result(keyword, offset=..., count=..., douyin_user_fans=..., douyin_user_type=..., search_id=...)` | `GET /api/v1/douyin/web/fetch_user_search_result` | 获取指定关键词的用户搜索结果(废弃，替代接口请参考下方文档)/Get user search results of specified keywords (deprecated, please refer to the following  |
| `fetch_user_search_result_v2(keyword, cursor=...)` | `GET /api/v1/douyin/web/fetch_user_search_result_v2` | 获取指定关键词的用户搜索结果 V2 (已弃用，替代接口请参考下方文档)/Get user search results of specified keywords V2 (deprecated, please refer to the fo |
| `fetch_user_search_result_v3(keyword, cursor=..., douyin_user_type=..., douyin_user_fans=...)` | `GET /api/v1/douyin/web/fetch_user_search_result_v3` | 获取指定关键词的用户搜索结果 V3 (已弃用，替代接口请参考下方文档)/Get user search results of specified keywords V3 (deprecated, please refer to the fo |
| `fetch_video_channel_result(tag_id, count=..., refresh_index=...)` | `GET /api/v1/douyin/web/fetch_video_channel_result` | 抖音视频频道数据/Douyin video channel data |
| `fetch_video_comment_replies(item_id, comment_id, cursor=..., count=...)` | `GET /api/v1/douyin/web/fetch_video_comment_replies` | 获取指定视频的评论回复数据/Get comment replies data of specified video |
| `fetch_video_comments(aweme_id, cursor=..., count=...)` | `GET /api/v1/douyin/web/fetch_video_comments` | 获取单个视频评论数据/Get single video comments data |
| `fetch_video_high_quality_play_url(aweme_id=..., share_url=...)` | `GET /api/v1/douyin/web/fetch_video_high_quality_play_url` | 获取视频的最高画质播放链接/Get the highest quality play URL of the video |
| `fetch_video_search_result(keyword, offset=..., count=..., sort_type=..., publish_time=..., filter_duration=..., search_id=...)` | `GET /api/v1/douyin/web/fetch_video_search_result` | [已弃用/Deprecated] 获取指定关键词的视频搜索结果/Get video search results of specified keywords |
| `fetch_video_search_result_v2(keyword, sort_type=..., publish_time=..., filter_duration=..., page=..., search_id=...)` | `GET /api/v1/douyin/web/fetch_video_search_result_v2` | 获取指定关键词的视频搜索结果 V2 （废弃，替代接口请参考下方文档）/Get video search results of specified keywords V2 (Deprecated, please refer to the fo |
| `generate_a_bogus(url, data, user_agent, index_0=..., index_1=..., index_2=...)` | `POST /api/v1/douyin/web/generate_a_bogus` | 使用接口网址生成A-Bogus参数/Generate A-Bogus parameter using API URL |
| `generate_real_msToken()` | `GET /api/v1/douyin/web/generate_real_msToken` | 生成真实msToken/Generate real msToken |
| `generate_s_v_web_id()` | `GET /api/v1/douyin/web/generate_s_v_web_id` | 生成s_v_web_id/Generate s_v_web_id |
| `generate_ttwid(user_agent=...)` | `GET /api/v1/douyin/web/generate_ttwid` | 生成ttwid/Generate ttwid |
| `generate_verify_fp()` | `GET /api/v1/douyin/web/generate_verify_fp` | 生成verify_fp/Generate verify_fp |
| `generate_wss_xb_signature(user_agent, room_id, user_unique_id)` | `GET /api/v1/douyin/web/generate_wss_xb_signature` | 生成弹幕xb签名/Generate barrage xb signature |
| `generate_x_bogus(url, user_agent)` | `POST /api/v1/douyin/web/generate_x_bogus` | 使用接口网址生成X-Bogus参数/Generate X-Bogus parameter using API URL |
| `get_all_aweme_id(body)` | `POST /api/v1/douyin/web/get_all_aweme_id` | 提取列表作品id/Extract list video id |
| `get_all_sec_user_id(body)` | `POST /api/v1/douyin/web/get_all_sec_user_id` | 提取列表用户id/Extract list user id |
| `get_all_webcast_id(body)` | `POST /api/v1/douyin/web/get_all_webcast_id` | 提取列表直播间号/Extract list webcast id |
| `get_aweme_id(url)` | `GET /api/v1/douyin/web/get_aweme_id` | 提取单个作品id/Extract single video id |
| `get_sec_user_id(url)` | `GET /api/v1/douyin/web/get_sec_user_id` | 提取单个用户id/Extract single user id |
| `get_webcast_id(url)` | `GET /api/v1/douyin/web/get_webcast_id` | 提取直播间号/Extract webcast id |
| `handler_shorten_url(target_url)` | `GET /api/v1/douyin/web/handler_shorten_url` | 生成短链接 |
| `handler_user_profile(sec_user_id)` | `GET /api/v1/douyin/web/handler_user_profile` | 使用sec_user_id获取指定用户的信息/Get information of specified user by sec_user_id |
| `handler_user_profile_v2(unique_id)` | `GET /api/v1/douyin/web/handler_user_profile_v2` | 使用unique_id（抖音号）获取指定用户的信息/Get information of specified user by unique_id |
| `handler_user_profile_v3(uid)` | `GET /api/v1/douyin/web/handler_user_profile_v3` | 根据抖音uid获取指定用户的信息/Get information of specified user by uid |
| `handler_user_profile_v4(sec_user_id)` | `GET /api/v1/douyin/web/handler_user_profile_v4` | 根据sec_user_id获取指定用户的信息（性别，年龄，直播等级、牌子）/Get information of specified user by sec_user_id (gender, age, live level、brand) |
| `webcast_id_2_room_id(webcast_id)` | `GET /api/v1/douyin/web/webcast_id_2_room_id` | 直播间号转房间号/Webcast id to room id |

## `client.douyin_xingtu`

**Class:** `tikhub.resources.douyin_xingtu.DouyinXingtu` (sync) / `AsyncDouyinXingtu` (async)

**Endpoints:** 22

| Method | Endpoint | Summary |
|---|---|---|
| `author_content_hot_comment_keywords_v1(kolId)` | `GET /api/v1/douyin/xingtu/author_content_hot_comment_keywords_v1` | 获取kol热词分析内容V1/Get Author Content Hot Comment Keywords V1 |
| `author_hot_comment_tokens_v1(kolId)` | `GET /api/v1/douyin/xingtu/author_hot_comment_tokens_v1` | 获取kol热词分析评论V1/Get Author Hot Comment Tokens V1 |
| `get_sign_image(uri, durationTS=..., format=...)` | `GET /api/v1/douyin/xingtu/get_sign_image` | 获取加密图片解析/Get Sign Image |
| `get_xingtu_kolid_by_sec_user_id(sec_user_id)` | `GET /api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id` | 根据抖音sec_user_id获取游客星图kolid/Get XingTu kolid by Douyin sec_user_id |
| `get_xingtu_kolid_by_uid(uid)` | `GET /api/v1/douyin/xingtu/get_xingtu_kolid_by_uid` | 根据抖音用户ID获取游客星图kolid/Get XingTu kolid by Douyin User ID |
| `get_xingtu_kolid_by_unique_id(unique_id)` | `GET /api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` | 根据抖音号获取游客星图kolid/Get XingTu kolid by Douyin unique_id |
| `kol_audience_portrait_v1(kolId)` | `GET /api/v1/douyin/xingtu/kol_audience_portrait_v1` | 获取kol观众画像V1/Get kol Audience Portrait V1 |
| `kol_base_info_v1(kolId, platformChannel)` | `GET /api/v1/douyin/xingtu/kol_base_info_v1` | 获取kol基本信息V1/Get kol Base Info V1 |
| `kol_conversion_ability_analysis_v1(kolId, _range)` | `GET /api/v1/douyin/xingtu/kol_conversion_ability_analysis_v1` | 获取kol转化能力分析V1/Get kol Conversion Ability Analysis V1 |
| `kol_convert_video_display_v1(kolId, detailType, page)` | `GET /api/v1/douyin/xingtu/kol_convert_video_display_v1` | 获取kol转化视频展示V1/Get kol Convert Video Display V1 |
| `kol_cp_info_v1(kolId)` | `GET /api/v1/douyin/xingtu/kol_cp_info_v1` | 获取kol性价比能力分析V1/Get kol Cp Info V1 |
| `kol_daily_fans_v1(kolId, startDate, endDate)` | `GET /api/v1/douyin/xingtu/kol_daily_fans_v1` | 获取kol粉丝趋势V1/Get kol Daily Fans V1 |
| `kol_data_overview_v1(kolId, _type, _range, flowType, onlyAssign=...)` | `GET /api/v1/douyin/xingtu/kol_data_overview_v1` | 获取kol数据概览V1/Get kol Data Overview V1 |
| `kol_fans_portrait_v1(kolId, fansType=...)` | `GET /api/v1/douyin/xingtu/kol_fans_portrait_v1` | 获取kol粉丝画像V1/Get kol Fans Portrait V1 |
| `kol_link_struct_v1(kolId)` | `GET /api/v1/douyin/xingtu/kol_link_struct_v1` | 获取kol连接用户V1/Get kol Link Struct V1 |
| `kol_rec_videos_v1(kolId)` | `GET /api/v1/douyin/xingtu/kol_rec_videos_v1` | 获取kol内容表现V1/Get kol Rec Videos V1 |
| `kol_service_price_v1(kolId, platformChannel)` | `GET /api/v1/douyin/xingtu/kol_service_price_v1` | 获取kol服务报价V1/Get kol Service Price V1 |
| `kol_touch_distribution_v1(kolId)` | `GET /api/v1/douyin/xingtu/kol_touch_distribution_v1` | 获取kol连接用户来源V1/Get kol Touch Distribution V1 |
| `kol_video_performance_v1(kolId, onlyAssign)` | `GET /api/v1/douyin/xingtu/kol_video_performance_v1` | 获取kol视频表现V1/Get kol Video Performance V1 |
| `kol_xingtu_index_v1(kolId)` | `GET /api/v1/douyin/xingtu/kol_xingtu_index_v1` | 获取kol星图指数V1/Get kol Xingtu Index V1 |
| `search_kol_v1(keyword, platformSource, page)` | `GET /api/v1/douyin/xingtu/search_kol_v1` | 关键词搜索kol V1/Search Kol V1 |
| `search_kol_v2(keyword, followerRange=..., contentTag=...)` | `GET /api/v1/douyin/xingtu/search_kol_v2` | 高级搜索kol V2/Search Kol Advanced V2 |

## `client.douyin_xingtu_v2`

**Class:** `tikhub.resources.douyin_xingtu_v2.DouyinXingtuV2` (sync) / `AsyncDouyinXingtuV2` (async)

**Endpoints:** 21

| Method | Endpoint | Summary |
|---|---|---|
| `get_author_base_info(o_author_id, platform_source=..., platform_channel=..., recommend=..., need_sec_uid=..., need_linkage_info=...)` | `GET /api/v1/douyin/xingtu_v2/get_author_base_info` | 获取创作者基本信息/Get Author Base Info |
| `get_author_business_card_info(o_author_id)` | `GET /api/v1/douyin/xingtu_v2/get_author_business_card_info` | 获取创作者商业卡片信息/Get Author Business Card Info |
| `get_author_content_hot_keywords(author_id, keyword_type=...)` | `GET /api/v1/douyin/xingtu_v2/get_author_content_hot_keywords` | 获取创作者内容热词/Get Author Content Hot Keywords |
| `get_author_hot_comment_tokens(author_id, num=..., without_emoji=...)` | `GET /api/v1/douyin/xingtu_v2/get_author_hot_comment_tokens` | 获取创作者评论热词/Get Author Hot Comment Tokens |
| `get_author_local_info(o_author_id, platform_source=..., platform_channel=..., time_range=...)` | `GET /api/v1/douyin/xingtu_v2/get_author_local_info` | 获取创作者位置信息/Get Author Local Info |
| `get_author_market_fields(market_scene=...)` | `GET /api/v1/douyin/xingtu_v2/get_author_market_fields` | 获取达人广场筛选字段/Get Author Market Fields |
| `get_author_show_items(o_author_id, platform_source=..., platform_channel=..., limit=..., only_assign=..., flow_type=...)` | `GET /api/v1/douyin/xingtu_v2/get_author_show_items` | 获取创作者视频列表/Get Author Show Items |
| `get_author_spread_info(o_author_id, platform_source=..., platform_channel=..., type=..., flow_type=..., only_assign=..., range=...)` | `GET /api/v1/douyin/xingtu_v2/get_author_spread_info` | 获取创作者传播价值/Get Author Spread Info |
| `get_content_trend_guide()` | `GET /api/v1/douyin/xingtu_v2/get_content_trend_guide` | 获取内容趋势指南/Get Content Trend Guide |
| `get_demander_mcn_list(mcn_name=..., page=..., limit=..., order_by=...)` | `GET /api/v1/douyin/xingtu_v2/get_demander_mcn_list` | 搜索MCN机构列表/Get Demander MCN List |
| `get_excellent_case_category_list(platform_source=...)` | `GET /api/v1/douyin/xingtu_v2/get_excellent_case_category_list` | 获取优秀行业分类列表/Get Excellent Case Category List |
| `get_ip_activity_detail(id)` | `GET /api/v1/douyin/xingtu_v2/get_ip_activity_detail` | 获取星图IP活动详情/Get IP Activity Detail |
| `get_ip_activity_industry_list()` | `GET /api/v1/douyin/xingtu_v2/get_ip_activity_industry_list` | 获取星图IP日历行业列表/Get IP Activity Industry List |
| `get_ip_activity_list(query_start_time, query_end_time, industry_id_list=..., category_list=..., status_list=...)` | `POST /api/v1/douyin/xingtu_v2/get_ip_activity_list` | 获取星图IP日历活动列表/Get IP Activity List |
| `get_playlet_actor_rank_catalog()` | `POST /api/v1/douyin/xingtu_v2/get_playlet_actor_rank_catalog` | 获取短剧演员热榜分类/Get Playlet Actor Rank Catalog |
| `get_playlet_actor_rank_list(category=..., name=..., qualifier=..., period=..., date=..., limit=...)` | `GET /api/v1/douyin/xingtu_v2/get_playlet_actor_rank_list` | 获取短剧演员热榜/Get Playlet Actor Rank List |
| `get_ranking_list_catalog(codes=..., biz_scene=...)` | `GET /api/v1/douyin/xingtu_v2/get_ranking_list_catalog` | 获取星图热榜分类/Get Ranking List Catalog |
| `get_ranking_list_data(code=..., qualifier=..., version=..., period=..., date=..., limit=...)` | `GET /api/v1/douyin/xingtu_v2/get_ranking_list_data` | 获取星图达人商业榜数据/Get Ranking List Data |
| `get_recommend_for_star_authors(author_ids, similar_type=..., page=..., limit=...)` | `POST /api/v1/douyin/xingtu_v2/get_recommend_for_star_authors` | 获取相似创作者推荐/Get Recommend Similar Star Authors |
| `get_resource_list(resource_id)` | `GET /api/v1/douyin/xingtu_v2/get_resource_list` | 获取营销活动案例/Get Resource List |
| `get_user_profile_qrcode(core_user_id=..., sec_uid=...)` | `GET /api/v1/douyin/xingtu_v2/get_user_profile_qrcode` | 获取用户主页二维码/Get User Profile QRCode |

## `client.health_check`

**Class:** `tikhub.resources.health_check.HealthCheck` (sync) / `AsyncHealthCheck` (async)

**Endpoints:** 1

| Method | Endpoint | Summary |
|---|---|---|
| `check()` | `GET /api/v1/health/check` | 检查服务器是否正确响应请求 / Check if the server responds to requests correctly |

## `client.hybrid_parsing`

**Class:** `tikhub.resources.hybrid_parsing.HybridParsing` (sync) / `AsyncHybridParsing` (async)

**Endpoints:** 1

| Method | Endpoint | Summary |
|---|---|---|
| `video_data(url, minimal=..., base64_url=...)` | `GET /api/v1/hybrid/video_data` | 混合解析单一视频接口/Hybrid parsing single video endpoint |

## `client.instagram_v1`

**Class:** `tikhub.resources.instagram_v1.InstagramV1` (sync) / `AsyncInstagramV1` (async)

**Endpoints:** 29

| Method | Endpoint | Summary |
|---|---|---|
| `fetch_cities(country_code, page=...)` | `GET /api/v1/instagram/v1/fetch_cities` | 获取国家城市列表/Get cities by country |
| `fetch_comment_replies(media_id, comment_id, min_id=...)` | `GET /api/v1/instagram/v1/fetch_comment_replies` | 获取评论的子评论列表/Get comment replies |
| `fetch_explore_sections()` | `GET /api/v1/instagram/v1/fetch_explore_sections` | 获取探索页面分类/Get explore page sections |
| `fetch_hashtag_posts(hashtag, end_cursor=...)` | `GET /api/v1/instagram/v1/fetch_hashtag_posts` | 获取话题标签下的帖子/Get posts by hashtag |
| `fetch_location_info(location_id)` | `GET /api/v1/instagram/v1/fetch_location_info` | 获取地点信息/Get location info |
| `fetch_location_posts(location_id, tab=..., end_cursor=...)` | `GET /api/v1/instagram/v1/fetch_location_posts` | 获取地点下的帖子/Get posts by location |
| `fetch_locations(city_id, page=...)` | `GET /api/v1/instagram/v1/fetch_locations` | 获取城市地点列表/Get locations by city |
| `fetch_music_posts(music_id=..., music_url=..., max_id=...)` | `GET /api/v1/instagram/v1/fetch_music_posts` | 获取使用特定音乐的帖子/Get posts using specific music |
| `fetch_post_by_id(post_id)` | `GET /api/v1/instagram/v1/fetch_post_by_id` | 通过ID获取帖子详情/Get post by ID |
| `fetch_post_by_url(post_url)` | `GET /api/v1/instagram/v1/fetch_post_by_url` | 通过URL获取帖子详情/Get post by URL |
| `fetch_post_by_url_v2(post_url)` | `GET /api/v1/instagram/v1/fetch_post_by_url_v2` | 通过URL获取帖子详情 V2/Get post by URL V2 |
| `fetch_post_comments_v2(media_id, sort_order=..., min_id=...)` | `GET /api/v1/instagram/v1/fetch_post_comments_v2` | 获取帖子评论列表V2/Get post comments V2 |
| `fetch_related_profiles(user_id)` | `GET /api/v1/instagram/v1/fetch_related_profiles` | 获取相关用户推荐/Get related profiles |
| `fetch_search(query, select=...)` | `GET /api/v1/instagram/v1/fetch_search` | 搜索用户/话题/地点/Search users/hashtags/places |
| `fetch_section_posts(section_id, count=..., max_id=...)` | `GET /api/v1/instagram/v1/fetch_section_posts` | 获取分类下的帖子/Get posts by section |
| `fetch_user_about_info(user_id)` | `GET /api/v1/instagram/v1/fetch_user_about_info` | 获取用户的About信息/Get user about info |
| `fetch_user_info_by_id(user_id)` | `GET /api/v1/instagram/v1/fetch_user_info_by_id` | 根据用户ID获取用户数据/Get user data by user ID |
| `fetch_user_info_by_id_v2(user_id)` | `GET /api/v1/instagram/v1/fetch_user_info_by_id_v2` | 根据用户ID获取用户数据V2/Get user data by user ID V2 |
| `fetch_user_info_by_username(username)` | `GET /api/v1/instagram/v1/fetch_user_info_by_username` | 根据用户名获取用户数据/Get user data by username |
| `fetch_user_info_by_username_v2(username)` | `GET /api/v1/instagram/v1/fetch_user_info_by_username_v2` | 根据用户名获取用户数据V2/Get user data by username V2 |
| `fetch_user_info_by_username_v3(username)` | `GET /api/v1/instagram/v1/fetch_user_info_by_username_v3` | 根据用户名获取用户数据V3/Get user data by username V3 |
| `fetch_user_posts(user_id, count=..., max_id=...)` | `GET /api/v1/instagram/v1/fetch_user_posts` | 获取用户帖子列表/Get user posts list |
| `fetch_user_posts_v2(user_id, count=..., end_cursor=...)` | `GET /api/v1/instagram/v1/fetch_user_posts_v2` | 获取用户帖子列表V2/Get user posts list V2 |
| `fetch_user_reels(user_id, count=..., max_id=...)` | `GET /api/v1/instagram/v1/fetch_user_reels` | 获取用户Reels列表/Get user Reels list |
| `fetch_user_reposts(user_id, max_id=...)` | `GET /api/v1/instagram/v1/fetch_user_reposts` | 获取用户转发列表/Get user reposts list |
| `fetch_user_tagged_posts(user_id, count=..., end_cursor=...)` | `GET /api/v1/instagram/v1/fetch_user_tagged_posts` | 获取用户被标记的帖子/Get user tagged posts |
| `media_id_to_shortcode(media_id)` | `GET /api/v1/instagram/v1/media_id_to_shortcode` | Media ID转Shortcode/Convert media ID to shortcode |
| `shortcode_to_media_id(shortcode)` | `GET /api/v1/instagram/v1/shortcode_to_media_id` | Shortcode转Media ID/Convert shortcode to media ID |
| `user_id_to_username(user_id)` | `GET /api/v1/instagram/v1/user_id_to_username` | 用户ID转用户信息/Get user info by user ID |

## `client.instagram_v2`

**Class:** `tikhub.resources.instagram_v2.InstagramV2` (sync) / `AsyncInstagramV2` (async)

**Endpoints:** 27

| Method | Endpoint | Summary |
|---|---|---|
| `fetch_comment_replies(code_or_url, comment_id, pagination_token=...)` | `GET /api/v1/instagram/v2/fetch_comment_replies` | 获取评论回复/Get comment replies |
| `fetch_hashtag_posts(keyword, feed_type=..., pagination_token=...)` | `GET /api/v1/instagram/v2/fetch_hashtag_posts` | 获取话题帖子/Get hashtag posts |
| `fetch_highlight_stories(highlight_id)` | `GET /api/v1/instagram/v2/fetch_highlight_stories` | 获取精选故事详情/Get highlight stories |
| `fetch_location_posts(location_id, pagination_token=...)` | `GET /api/v1/instagram/v2/fetch_location_posts` | 获取地点帖子/Get location posts |
| `fetch_music_posts(audio_canonical_id, pagination_token=...)` | `GET /api/v1/instagram/v2/fetch_music_posts` | 获取音乐帖子/Get music posts |
| `fetch_post_comments(code_or_url, sort_by=..., pagination_token=...)` | `GET /api/v1/instagram/v2/fetch_post_comments` | 获取帖子评论/Get post comments |
| `fetch_post_info(code_or_url)` | `GET /api/v1/instagram/v2/fetch_post_info` | 获取帖子详情/Get post info |
| `fetch_post_likes(code_or_url, end_cursor=...)` | `GET /api/v1/instagram/v2/fetch_post_likes` | 获取帖子点赞列表/Get post likes |
| `fetch_similar_users(username=..., user_id=...)` | `GET /api/v1/instagram/v2/fetch_similar_users` | 获取相似用户/Get similar users |
| `fetch_user_followers(username=..., user_id=..., pagination_token=...)` | `GET /api/v1/instagram/v2/fetch_user_followers` | 获取用户粉丝/Get user followers |
| `fetch_user_following(username=..., user_id=..., pagination_token=...)` | `GET /api/v1/instagram/v2/fetch_user_following` | 获取用户关注/Get user following |
| `fetch_user_highlights(username=..., user_id=...)` | `GET /api/v1/instagram/v2/fetch_user_highlights` | 获取用户精选/Get user highlights |
| `fetch_user_info(username=..., user_id=...)` | `GET /api/v1/instagram/v2/fetch_user_info` | 获取用户信息/Get user info |
| `fetch_user_posts(username=..., user_id=..., pagination_token=...)` | `GET /api/v1/instagram/v2/fetch_user_posts` | 获取用户帖子/Get user posts |
| `fetch_user_reels(username=..., user_id=..., pagination_token=...)` | `GET /api/v1/instagram/v2/fetch_user_reels` | 获取用户Reels/Get user reels |
| `fetch_user_stories(username=..., user_id=...)` | `GET /api/v1/instagram/v2/fetch_user_stories` | 获取用户故事/Get user stories |
| `fetch_user_tagged_posts(username=..., user_id=..., pagination_token=...)` | `GET /api/v1/instagram/v2/fetch_user_tagged_posts` | 获取用户被标记的帖子/Get user tagged posts |
| `general_search(keyword, pagination_token=...)` | `GET /api/v1/instagram/v2/general_search` | 综合搜索/General search |
| `media_id_to_shortcode(media_id)` | `GET /api/v1/instagram/v2/media_id_to_shortcode` | Media ID转Shortcode/Convert media ID to shortcode |
| `search_by_coordinates(latitude, longitude)` | `GET /api/v1/instagram/v2/search_by_coordinates` | 根据坐标搜索地点/Search locations by coordinates |
| `search_hashtags(keyword)` | `GET /api/v1/instagram/v2/search_hashtags` | 搜索话题标签/Search hashtags |
| `search_locations(keyword)` | `GET /api/v1/instagram/v2/search_locations` | 搜索地点/Search locations |
| `search_music(keyword)` | `GET /api/v1/instagram/v2/search_music` | 搜索音乐/Search music |
| `search_reels(keyword, pagination_token=...)` | `GET /api/v1/instagram/v2/search_reels` | 搜索Reels/Search reels |
| `search_users(keyword)` | `GET /api/v1/instagram/v2/search_users` | 搜索用户/Search users |
| `shortcode_to_media_id(shortcode)` | `GET /api/v1/instagram/v2/shortcode_to_media_id` | Shortcode转Media ID/Convert shortcode to media ID |
| `user_id_to_username(user_id)` | `GET /api/v1/instagram/v2/user_id_to_username` | 用户ID转用户信息/Get user info by user ID |

## `client.instagram_v3`

**Class:** `tikhub.resources.instagram_v3.InstagramV3` (sync) / `AsyncInstagramV3` (async)

**Endpoints:** 32

| Method | Endpoint | Summary |
|---|---|---|
| `bulk_translate_comments(comment_ids)` | `GET /api/v1/instagram/v3/bulk_translate_comments` | 批量翻译评论/Bulk translate comments |
| `extract_shortcode(url)` | `GET /api/v1/instagram/v3/extract_shortcode` | 从URL提取短码/Extract shortcode from URL |
| `general_search(query, next_max_id=..., rank_token=..., enable_metadata=...)` | `GET /api/v1/instagram/v3/general_search` | 综合搜索（支持分页）/General search (with pagination) |
| `get_comment_replies(media_id, comment_id, min_id=...)` | `GET /api/v1/instagram/v3/get_comment_replies` | 获取评论的子评论/回复/Get comment replies |
| `get_explore(max_id=...)` | `GET /api/v1/instagram/v3/get_explore` | 获取探索页推荐帖子/Get explore feed |
| `get_highlight_stories(highlight_id, reel_ids=..., first=..., last=...)` | `GET /api/v1/instagram/v3/get_highlight_stories` | 获取Highlight精选详情/Get highlight stories |
| `get_location_info(location_id, show_nearby=...)` | `GET /api/v1/instagram/v3/get_location_info` | 获取地点详情/Get location info |
| `get_location_nearby(location_id)` | `GET /api/v1/instagram/v3/get_location_nearby` | 获取地点附近内容/Get nearby location content |
| `get_location_posts(location_id, tab=..., first=..., after=..., page_size_override=...)` | `GET /api/v1/instagram/v3/get_location_posts` | 获取地点相关帖子/Get location posts |
| `get_post_comments(code, min_id=..., sort_order=...)` | `GET /api/v1/instagram/v3/get_post_comments` | 获取帖子评论/Get post comments |
| `get_post_info(media_id)` | `GET /api/v1/instagram/v3/get_post_info` | 获取帖子详情/Get post info (media_id or URL) |
| `get_post_info_by_code(code)` | `GET /api/v1/instagram/v3/get_post_info_by_code` | 获取帖子详情(code)/Get post info by shortcode |
| `get_post_oembed(url, hidecaption=..., maxwidth=...)` | `GET /api/v1/instagram/v3/get_post_oembed` | 获取帖子oEmbed内嵌信息/Get post oEmbed info |
| `get_recommended_reels(first=..., after=...)` | `GET /api/v1/instagram/v3/get_recommended_reels` | 获取Reels推荐列表/Get recommended Reels feed |
| `get_user_about(user_id=..., username=...)` | `GET /api/v1/instagram/v3/get_user_about` | 获取用户账户简介/Get user about info |
| `get_user_brief(user_id, username)` | `GET /api/v1/instagram/v3/get_user_brief` | 获取用户短详情/Get user brief info |
| `get_user_followers(user_id=..., username=..., count=..., max_id=...)` | `GET /api/v1/instagram/v3/get_user_followers` | 获取用户粉丝列表/Get user followers list |
| `get_user_following(user_id=..., username=..., count=..., max_id=...)` | `GET /api/v1/instagram/v3/get_user_following` | 获取用户关注列表/Get user following list |
| `get_user_former_usernames(user_id=..., username=...)` | `GET /api/v1/instagram/v3/get_user_former_usernames` | 获取用户曾用用户名/Get user former usernames |
| `get_user_highlights(user_id=..., username=..., first=..., after=..., before=..., last=...)` | `GET /api/v1/instagram/v3/get_user_highlights` | 获取用户精选Highlights列表/Get user highlights |
| `get_user_id_by_username(username)` | `GET /api/v1/instagram/v3/get_user_id_by_username` | 通过用户名获取用户ID/Get user ID by username |
| `get_user_posts(username, first=..., after=..., before=..., last=..., count=...)` | `GET /api/v1/instagram/v3/get_user_posts` | 获取用户帖子列表/Get user posts |
| `get_user_profile(user_id=..., username=...)` | `GET /api/v1/instagram/v3/get_user_profile` | 获取用户信息/Get user profile |
| `get_user_reels(user_id=..., username=..., first=..., after=..., before=..., last=..., page_size=...)` | `GET /api/v1/instagram/v3/get_user_reels` | 获取用户Reels列表/Get user reels |
| `get_user_stories(user_id=..., username=...)` | `GET /api/v1/instagram/v3/get_user_stories` | 获取用户Stories（快拍）/Get user stories |
| `get_user_tagged_posts(user_id=..., username=..., first=..., after=..., before=..., last=..., count=...)` | `GET /api/v1/instagram/v3/get_user_tagged_posts` | 获取用户被标记的帖子/Get user tagged posts |
| `media_id_to_shortcode(media_id)` | `GET /api/v1/instagram/v3/media_id_to_shortcode` | 媒体ID转短码/Convert media ID to shortcode |
| `search_hashtags(query, rank_token=...)` | `GET /api/v1/instagram/v3/search_hashtags` | 搜索话题标签/Search hashtags |
| `search_places(query, rank_token=...)` | `GET /api/v1/instagram/v3/search_places` | 搜索地点/Search places |
| `search_users(query, rank_token=...)` | `GET /api/v1/instagram/v3/search_users` | 搜索用户/Search users |
| `shortcode_to_media_id(shortcode)` | `GET /api/v1/instagram/v3/shortcode_to_media_id` | 短码转媒体ID/Convert shortcode to media ID |
| `translate_comment(comment_id)` | `GET /api/v1/instagram/v3/translate_comment` | 翻译评论/帖子文本/Translate comment or caption |

## `client.ios_shortcut`

**Class:** `tikhub.resources.ios_shortcut.IosShortcut` (sync) / `AsyncIosShortcut` (async)

**Endpoints:** 1

| Method | Endpoint | Summary |
|---|---|---|
| `shortcut()` | `GET /api/v1/ios_shortcut/shortcut` | 用于iOS快捷指令的版本更新信息/Version update information for iOS shortcuts |

## `client.kuaishou_app`

**Class:** `tikhub.resources.kuaishou_app.KuaishouApp` (sync) / `AsyncKuaishouApp` (async)

**Endpoints:** 20

| Method | Endpoint | Summary |
|---|---|---|
| `fetch_brand_top_list(subTabId=..., subTabName=...)` | `GET /api/v1/kuaishou/app/fetch_brand_top_list` | 快手品牌榜单/Kuaishou brand top list |
| `fetch_hot_board_categories()` | `GET /api/v1/kuaishou/app/fetch_hot_board_categories` | 快手热榜分类/Kuaishou hot categories |
| `fetch_hot_board_detail(boardType=..., boardId=...)` | `GET /api/v1/kuaishou/app/fetch_hot_board_detail` | 快手热榜详情/Kuaishou hot board detail |
| `fetch_hot_search_person()` | `GET /api/v1/kuaishou/app/fetch_hot_search_person` | 快手热搜人物榜单/Kuaishou hot search person board |
| `fetch_live_top_list(subTabId=..., subTabName=...)` | `GET /api/v1/kuaishou/app/fetch_live_top_list` | 快手直播榜单/Kuaishou live top list |
| `fetch_magic_face_hot(magic_face_id, pcursor=..., count=...)` | `GET /api/v1/kuaishou/app/fetch_magic_face_hot` | 获取魔法表情热门视频/Fetch magic face hot videos |
| `fetch_magic_face_usage(magic_face_id)` | `GET /api/v1/kuaishou/app/fetch_magic_face_usage` | 获取魔法表情使用人数/Fetch magic face usage count |
| `fetch_one_user_v2(user_id)` | `GET /api/v1/kuaishou/app/fetch_one_user_v2` | 获取单个用户数据V2/Get single user data V2 |
| `fetch_one_video(photo_id)` | `GET /api/v1/kuaishou/app/fetch_one_video` | 视频详情V1/Video detailsV1 |
| `fetch_one_video_by_url(share_text)` | `GET /api/v1/kuaishou/app/fetch_one_video_by_url` | 根据链接获取单个作品数据/Fetch single video by URL |
| `fetch_one_video_comment(photo_id, pcursor=...)` | `GET /api/v1/kuaishou/app/fetch_one_video_comment` | 获取单个作品评论数据/Get single video comment data |
| `fetch_shopping_top_list(subTabId=..., subTabName=...)` | `GET /api/v1/kuaishou/app/fetch_shopping_top_list` | 快手购物榜单/Kuaishou shopping top list |
| `fetch_user_hot_post(user_id, pcursor=...)` | `GET /api/v1/kuaishou/app/fetch_user_hot_post` | 获取用户热门作品数据/Get user hot post data |
| `fetch_user_live_info(user_id)` | `GET /api/v1/kuaishou/app/fetch_user_live_info` | 获取用户直播信息/Get user live info |
| `fetch_user_post_v2(user_id, pcursor=...)` | `GET /api/v1/kuaishou/app/fetch_user_post_v2` | 用户视频列表V2/User video list V2 |
| `fetch_videos_batch(photo_ids)` | `GET /api/v1/kuaishou/app/fetch_videos_batch` | 快手批量视频查询接口/Kuaishou batch video query API |
| `generate_kuaishou_share_link(shareObjectId)` | `GET /api/v1/kuaishou/app/generate_kuaishou_share_link` | 生成快手分享链接/Generate Kuaishou share link |
| `search_comprehensive(keyword, pcursor=..., sort_type=..., publish_time=..., duration=..., search_scope=...)` | `GET /api/v1/kuaishou/app/search_comprehensive` | 综合搜索/Comprehensive search |
| `search_user_v2(keyword, page=...)` | `GET /api/v1/kuaishou/app/search_user_v2` | 搜索用户V2/Search user V2 |
| `search_video_v2(keyword, page=...)` | `GET /api/v1/kuaishou/app/search_video_v2` | 搜索视频V2/Search video V2 |

## `client.kuaishou_web`

**Class:** `tikhub.resources.kuaishou_web.KuaishouWeb` (sync) / `AsyncKuaishouWeb` (async)

**Endpoints:** 13

| Method | Endpoint | Summary |
|---|---|---|
| `fetch_get_user_id(share_link)` | `GET /api/v1/kuaishou/web/fetch_get_user_id` | 获取用户ID/Fetch user ID |
| `fetch_kuaishou_hot_list_v1()` | `GET /api/v1/kuaishou/web/fetch_kuaishou_hot_list_v1` | 获取快手热榜 V1/Fetch Kuaishou Hot List V1 |
| `fetch_kuaishou_hot_list_v2(board_type=...)` | `GET /api/v1/kuaishou/web/fetch_kuaishou_hot_list_v2` | 获取快手热榜 V2/Fetch Kuaishou Hot List V2 |
| `fetch_one_video(share_text)` | `GET /api/v1/kuaishou/web/fetch_one_video` | 获取单个作品数据 V1/Get single video data V1 |
| `fetch_one_video_by_url(url)` | `GET /api/v1/kuaishou/web/fetch_one_video_by_url` | 链接获取作品数据/Fetch single video by URL |
| `fetch_one_video_comment(photo_id, pcursor=...)` | `GET /api/v1/kuaishou/web/fetch_one_video_comment` | 获取作品一级评论/Fetch video comments |
| `fetch_one_video_sub_comment(photo_id, root_comment_id, pcursor=...)` | `GET /api/v1/kuaishou/web/fetch_one_video_sub_comment` | 获取作品二级评论/Fetch video sub comments |
| `fetch_one_video_v2(photo_id)` | `GET /api/v1/kuaishou/web/fetch_one_video_v2` | 获取单个作品数据 V2/Get single video data V2 |
| `fetch_user_collect(user_id, pcursor=...)` | `GET /api/v1/kuaishou/web/fetch_user_collect` | 获取用户收藏作品/Fetch user collect |
| `fetch_user_info(user_id)` | `GET /api/v1/kuaishou/web/fetch_user_info` | 获取用户信息/Fetch user info |
| `fetch_user_live_replay(user_id, pcursor=...)` | `GET /api/v1/kuaishou/web/fetch_user_live_replay` | 获取用户直播回放/Fetch user live replay |
| `fetch_user_post(user_id, pcursor=...)` | `GET /api/v1/kuaishou/web/fetch_user_post` | 获取用户发布作品/Fetch user posts |
| `generate_share_short_url(photo_id)` | `GET /api/v1/kuaishou/web/generate_share_short_url` | 生成分享短连接/Generate share short URL |

## `client.lemon8_app`

**Class:** `tikhub.resources.lemon8_app.Lemon8App` (sync) / `AsyncLemon8App` (async)

**Endpoints:** 16

| Method | Endpoint | Summary |
|---|---|---|
| `fetch_discover_banners()` | `GET /api/v1/lemon8/app/fetch_discover_banners` | 获取发现页Banner/Get banners of discover page |
| `fetch_discover_tab()` | `GET /api/v1/lemon8/app/fetch_discover_tab` | 获取发现页主体内容/Get main content of discover page |
| `fetch_discover_tab_information_tabs()` | `GET /api/v1/lemon8/app/fetch_discover_tab_information_tabs` | 获取发现页的 Editor's Picks/Get Editor's Picks of discover page |
| `fetch_hot_search_keywords()` | `GET /api/v1/lemon8/app/fetch_hot_search_keywords` | 获取热搜关键词/Get hot search keywords |
| `fetch_post_comment_list(group_id, item_id, media_id, offset=...)` | `GET /api/v1/lemon8/app/fetch_post_comment_list` | 获取指定作品的评论列表/Get comments list of specified post |
| `fetch_post_detail(item_id)` | `GET /api/v1/lemon8/app/fetch_post_detail` | 获取指定作品的信息/Get information of specified post |
| `fetch_search(query, max_cursor=..., filter_type=..., order_by=..., search_tab=...)` | `GET /api/v1/lemon8/app/fetch_search` | 搜索接口/Search API |
| `fetch_topic_info(forum_id)` | `GET /api/v1/lemon8/app/fetch_topic_info` | 获取话题信息/Get topic information |
| `fetch_topic_post_list(category, category_parameter, hashtag_name, max_behot_time=..., sort_type=...)` | `GET /api/v1/lemon8/app/fetch_topic_post_list` | 获取话题作品列表/Get topic post list |
| `fetch_user_follower_list(user_id, cursor=...)` | `GET /api/v1/lemon8/app/fetch_user_follower_list` | 获取指定用户的粉丝列表/Get fans list of specified user |
| `fetch_user_following_list(user_id, cursor=...)` | `GET /api/v1/lemon8/app/fetch_user_following_list` | 获取指定用户的关注列表/Get following list of specified user |
| `fetch_user_profile(user_id)` | `GET /api/v1/lemon8/app/fetch_user_profile` | 获取指定用户的信息/Get information of specified user |
| `get_item_id(share_text)` | `GET /api/v1/lemon8/app/get_item_id` | 通过分享链接获取作品ID/Get post ID through sharing link |
| `get_item_ids(body)` | `POST /api/v1/lemon8/app/get_item_ids` | 通过分享链接批量获取作品ID/Get post IDs in batch through sharing links |
| `get_user_id(share_text)` | `GET /api/v1/lemon8/app/get_user_id` | 通过分享链接获取用户ID/Get user ID through sharing link |
| `get_user_ids(body)` | `POST /api/v1/lemon8/app/get_user_ids` | 通过分享链接批量获取用户ID/Get user IDs in batch through sharing links |

## `client.linkedin_web`

**Class:** `tikhub.resources.linkedin_web.LinkedinWeb` (sync) / `AsyncLinkedinWeb` (async)

**Endpoints:** 25

| Method | Endpoint | Summary |
|---|---|---|
| `get_company_job_count(company_id)` | `GET /api/v1/linkedin/web/get_company_job_count` | 获取公司职位数量/Get company job count |
| `get_company_jobs(company_id, page=..., sort_by=..., date_posted=..., experience_level=..., remote=..., job_type=..., easy_apply=..., under_10_applicants=..., fair_chance_employer=...)` | `GET /api/v1/linkedin/web/get_company_jobs` | 获取公司职位/Get company jobs |
| `get_company_people(company_id, page=...)` | `GET /api/v1/linkedin/web/get_company_people` | 获取公司员工/Get company people |
| `get_company_posts(company_id, page=..., sort_by=...)` | `GET /api/v1/linkedin/web/get_company_posts` | 获取公司帖子/Get company posts |
| `get_company_profile(company=..., company_id=...)` | `GET /api/v1/linkedin/web/get_company_profile` | 获取公司资料/Get company profile |
| `get_job_detail(job_id, include_skills=...)` | `GET /api/v1/linkedin/web/get_job_detail` | 获取职位详情/Get job detail |
| `get_user_about(urn)` | `GET /api/v1/linkedin/web/get_user_about` | 获取用户简介/Get user about |
| `get_user_certifications(urn, page=...)` | `GET /api/v1/linkedin/web/get_user_certifications` | 获取用户认证/Get user certifications |
| `get_user_comments(urn, page=..., pagination_token=...)` | `GET /api/v1/linkedin/web/get_user_comments` | 获取用户评论/Get user comments |
| `get_user_contact(username)` | `GET /api/v1/linkedin/web/get_user_contact` | 获取用户联系信息/Get user contact information |
| `get_user_educations(urn, page=...)` | `GET /api/v1/linkedin/web/get_user_educations` | 获取用户教育背景/Get user educations |
| `get_user_experience(urn, page=...)` | `GET /api/v1/linkedin/web/get_user_experience` | 获取用户工作经历/Get user experience |
| `get_user_follower_and_connection(username)` | `GET /api/v1/linkedin/web/get_user_follower_and_connection` | 获取用户粉丝和连接数/Get user follower and connection |
| `get_user_honors(urn, page=...)` | `GET /api/v1/linkedin/web/get_user_honors` | 获取用户荣誉奖项/Get user honors |
| `get_user_images(urn, page=..., pagination_token=...)` | `GET /api/v1/linkedin/web/get_user_images` | 获取用户图片/Get user images |
| `get_user_interests_companies(urn, page=...)` | `GET /api/v1/linkedin/web/get_user_interests_companies` | 获取用户感兴趣的公司/Get user interests companies |
| `get_user_interests_groups(urn, page=...)` | `GET /api/v1/linkedin/web/get_user_interests_groups` | 获取用户感兴趣的群组/Get user interests groups |
| `get_user_posts(urn, page=..., pagination_token=...)` | `GET /api/v1/linkedin/web/get_user_posts` | 获取用户帖子/Get user posts |
| `get_user_profile(username, include_follower_and_connection=..., include_experiences=..., include_skills=..., include_certifications=..., include_publications=..., include_educations=..., include_volunteers=..., include_honors=..., include_interests=..., include_bio=...)` | `GET /api/v1/linkedin/web/get_user_profile` | 获取用户资料/Get user profile |
| `get_user_publications(urn, page=...)` | `GET /api/v1/linkedin/web/get_user_publications` | 获取用户出版物/Get user publications |
| `get_user_recommendations(urn, page=..., type=..., pagination_token=...)` | `GET /api/v1/linkedin/web/get_user_recommendations` | 获取用户推荐信/Get user recommendations |
| `get_user_skills(urn, page=...)` | `GET /api/v1/linkedin/web/get_user_skills` | 获取用户技能/Get user skills |
| `get_user_videos(urn, page=..., pagination_token=...)` | `GET /api/v1/linkedin/web/get_user_videos` | 获取用户视频/Get user videos |
| `search_jobs(keyword, page=..., sort_by=..., date_posted=..., geocode=..., company=..., experience_level=..., remote=..., job_type=..., easy_apply=..., has_verifications=..., under_10_applicants=..., fair_chance_employer=...)` | `GET /api/v1/linkedin/web/search_jobs` | 搜索职位/Search jobs |
| `search_people(name=..., first_name=..., last_name=..., title=..., company=..., school=..., page=..., geocode_location=..., current_company=..., profile_language=..., industry=..., service_category=...)` | `GET /api/v1/linkedin/web/search_people` | 搜索用户/Search people |

## `client.pipixia_app`

**Class:** `tikhub.resources.pipixia_app.PipixiaApp` (sync) / `AsyncPipixiaApp` (async)

**Endpoints:** 17

| Method | Endpoint | Summary |
|---|---|---|
| `fetch_hashtag_detail(hashtag_id)` | `GET /api/v1/pipixia/app/fetch_hashtag_detail` | 获取话题详情/Get hashtag detail |
| `fetch_hashtag_post_list(hashtag_id, cursor=..., feed_count=..., hashtag_request_type=..., hashtag_sort_type=...)` | `GET /api/v1/pipixia/app/fetch_hashtag_post_list` | 获取话题作品列表/Get hashtag post list |
| `fetch_home_feed(cursor=...)` | `GET /api/v1/pipixia/app/fetch_home_feed` | 获取首页推荐/Get home feed |
| `fetch_home_short_drama_feed(page=...)` | `GET /api/v1/pipixia/app/fetch_home_short_drama_feed` | 获取首页短剧推荐/Get home short drama feed |
| `fetch_hot_search_board_detail(block_type)` | `GET /api/v1/pipixia/app/fetch_hot_search_board_detail` | 获取热搜榜单详情/Get hot search board detail |
| `fetch_hot_search_board_list()` | `GET /api/v1/pipixia/app/fetch_hot_search_board_list` | 获取热搜榜单列表/Get hot search board list |
| `fetch_hot_search_words()` | `GET /api/v1/pipixia/app/fetch_hot_search_words` | 获取热搜词条/Get hot search words |
| `fetch_increase_post_view_count(cell_id, cell_type=...)` | `GET /api/v1/pipixia/app/fetch_increase_post_view_count` | 增加作品浏览数/Increase post view count |
| `fetch_post_comment_list(cell_id, cell_type=..., offset=...)` | `GET /api/v1/pipixia/app/fetch_post_comment_list` | 获取作品评论列表/Get post comment list |
| `fetch_post_detail(cell_id, cell_type=...)` | `GET /api/v1/pipixia/app/fetch_post_detail` | 获取单个作品数据/Get single video data |
| `fetch_post_statistics(cell_id)` | `GET /api/v1/pipixia/app/fetch_post_statistics` | 获取作品统计数据/Get post statistics |
| `fetch_search(keyword, offset=..., search_type=...)` | `GET /api/v1/pipixia/app/fetch_search` | 搜索接口/Search API |
| `fetch_short_url(original_url)` | `GET /api/v1/pipixia/app/fetch_short_url` | 生成短连接/Generate short URL |
| `fetch_user_follower_list(user_id, cursor=...)` | `GET /api/v1/pipixia/app/fetch_user_follower_list` | 获取用户粉丝列表/Get user follower list |
| `fetch_user_following_list(user_id, cursor=...)` | `GET /api/v1/pipixia/app/fetch_user_following_list` | 获取用户关注列表/Get user following list |
| `fetch_user_info(user_id)` | `GET /api/v1/pipixia/app/fetch_user_info` | 获取用户信息/Get user information |
| `fetch_user_post_list(user_id, cursor=..., feed_count=...)` | `GET /api/v1/pipixia/app/fetch_user_post_list` | 获取用户作品列表/Get user post list |

## `client.reddit_app`

**Class:** `tikhub.resources.reddit_app.RedditApp` (sync) / `AsyncRedditApp` (async)

**Endpoints:** 24

| Method | Endpoint | Summary |
|---|---|---|
| `check_subreddit_muted(subreddit_id, need_format=...)` | `GET /api/v1/reddit/app/check_subreddit_muted` | 检查版块是否静音/Check if Subreddit is Muted |
| `fetch_comment_replies(post_id, cursor, sort_type=..., need_format=...)` | `GET /api/v1/reddit/app/fetch_comment_replies` | 获取Reddit APP评论回复（二级评论）/Fetch Reddit APP Comment Replies (Sub-comments) |
| `fetch_community_highlights(subreddit_id, need_format=...)` | `GET /api/v1/reddit/app/fetch_community_highlights` | 获取Reddit APP社区亮点/Fetch Reddit APP Community Highlights |
| `fetch_dynamic_search(query, search_type=..., sort=..., time_range=..., safe_search=..., allow_nsfw=..., after=..., need_format=...)` | `GET /api/v1/reddit/app/fetch_dynamic_search` | 获取Reddit APP动态搜索结果/Fetch Reddit APP Dynamic Search Results |
| `fetch_games_feed(sort=..., time=..., after=..., need_format=...)` | `GET /api/v1/reddit/app/fetch_games_feed` | 获取Reddit APP游戏推荐内容/Fetch Reddit APP Games Feed |
| `fetch_home_feed(sort=..., filter_posts=..., after=..., need_format=...)` | `GET /api/v1/reddit/app/fetch_home_feed` | 获取Reddit APP首页推荐内容/Fetch Reddit APP Home Feed |
| `fetch_news_feed(subtopic_ids=..., after=..., need_format=...)` | `GET /api/v1/reddit/app/fetch_news_feed` | 获取Reddit APP资讯推荐内容/Fetch Reddit APP News Feed |
| `fetch_popular_feed(sort=..., time=..., filter_posts=..., after=..., need_format=...)` | `GET /api/v1/reddit/app/fetch_popular_feed` | 获取Reddit APP流行推荐内容/Fetch Reddit APP Popular Feed |
| `fetch_post_comments(post_id, sort_type=..., after=..., need_format=...)` | `GET /api/v1/reddit/app/fetch_post_comments` | 获取Reddit APP帖子评论/Fetch Reddit APP Post Comments |
| `fetch_post_details(post_id, include_comment_id=..., comment_id=..., need_format=...)` | `GET /api/v1/reddit/app/fetch_post_details` | 获取单个Reddit帖子详情/Fetch Single Reddit Post Details |
| `fetch_post_details_batch(post_ids, include_comment_id=..., comment_id=..., need_format=...)` | `GET /api/v1/reddit/app/fetch_post_details_batch` | 批量获取Reddit帖子详情(最多5条)/Fetch Reddit Post Details in Batch (Max 5) |
| `fetch_post_details_batch_large(post_ids, include_comment_id=..., comment_id=..., need_format=...)` | `GET /api/v1/reddit/app/fetch_post_details_batch_large` | 大批量获取Reddit帖子详情(最多30条)/Fetch Reddit Post Details in Large Batch (Max 30) |
| `fetch_search_typeahead(query, safe_search=..., allow_nsfw=..., need_format=...)` | `GET /api/v1/reddit/app/fetch_search_typeahead` | 获取Reddit APP搜索自动补全建议/Fetch Reddit APP Search Typeahead Suggestions |
| `fetch_subreddit_feed(subreddit_name, sort=..., filter_posts=..., after=..., need_format=...)` | `GET /api/v1/reddit/app/fetch_subreddit_feed` | 获取Reddit APP版块Feed内容/Fetch Reddit APP Subreddit Feed |
| `fetch_subreddit_info(subreddit_name=..., need_format=...)` | `GET /api/v1/reddit/app/fetch_subreddit_info` | 获取Reddit APP版块信息/Fetch Reddit APP Subreddit Info |
| `fetch_subreddit_post_channels(subreddit_name=..., sort=..., range=..., need_format=...)` | `GET /api/v1/reddit/app/fetch_subreddit_post_channels` | 获取Reddit APP版块帖子频道信息/Fetch Reddit APP Subreddit Post Channels |
| `fetch_subreddit_settings(subreddit_id, need_format=...)` | `GET /api/v1/reddit/app/fetch_subreddit_settings` | 获取Reddit APP版块设置/Fetch Reddit APP Subreddit Settings |
| `fetch_subreddit_style(subreddit_name=..., need_format=...)` | `GET /api/v1/reddit/app/fetch_subreddit_style` | 获取Reddit APP版块规则样式信息/Fetch Reddit APP Subreddit Rules and Style Info |
| `fetch_trending_searches(need_format=...)` | `GET /api/v1/reddit/app/fetch_trending_searches` | 获取Reddit APP今日热门搜索/Fetch Reddit APP Trending Searches |
| `fetch_user_active_subreddits(username, need_format=...)` | `GET /api/v1/reddit/app/fetch_user_active_subreddits` | 获取用户活跃的社区列表/Fetch User's Active Subreddits |
| `fetch_user_comments(username, sort=..., page_size=..., after=..., need_format=...)` | `GET /api/v1/reddit/app/fetch_user_comments` | 获取用户评论列表/Fetch User Comments |
| `fetch_user_posts(username, sort=..., after=..., need_format=...)` | `GET /api/v1/reddit/app/fetch_user_posts` | 获取用户发布的帖子列表/Fetch User Posts |
| `fetch_user_profile(username, need_format=...)` | `GET /api/v1/reddit/app/fetch_user_profile` | 获取Reddit APP用户资料信息/Fetch Reddit APP User Profile |
| `fetch_user_trophies(username, need_format=...)` | `GET /api/v1/reddit/app/fetch_user_trophies` | 获取用户公开奖杯/Fetch User Public Trophies |

## `client.sora2`

**Class:** `tikhub.resources.sora2.Sora2` (sync) / `AsyncSora2` (async)

**Endpoints:** 17

| Method | Endpoint | Summary |
|---|---|---|
| `create_video(prompt, orientation=..., media_id=...)` | `POST /api/v1/sora2/create_video` | [已弃用/Deprecated] 文本/图片生成视频/Create video from text or image |
| `get_cameo_leaderboard(cursor=...)` | `GET /api/v1/sora2/get_cameo_leaderboard` | 获取 Cameo 出镜秀达人排行榜/Fetch Cameo leaderboard |
| `get_comment_replies(comment_id, cursor=...)` | `GET /api/v1/sora2/get_comment_replies` | 获取评论的回复/Fetch comment replies |
| `get_feed(cursor=..., eager_views=...)` | `GET /api/v1/sora2/get_feed` | 获取Feed流（热门/推荐视频）/Fetch feed |
| `get_post_comments(post_id, cursor=...)` | `GET /api/v1/sora2/get_post_comments` | 获取作品一级评论/Fetch post comments |
| `get_post_detail(post_id=..., post_url=...)` | `GET /api/v1/sora2/get_post_detail` | 获取单一作品详情/Fetch single post detail |
| `get_post_remix_list(post_id=..., post_url=..., cursor=...)` | `GET /api/v1/sora2/get_post_remix_list` | 获取作品的 Remix 列表/Fetch post remix list |
| `get_task_detail(task_id=..., generation_id=...)` | `GET /api/v1/sora2/get_task_detail` | [已弃用/Deprecated] 获取任务生成的作品详情（无水印版本）/Get task-generated post detail (watermark-free) |
| `get_task_status(task_id)` | `GET /api/v1/sora2/get_task_status` | [已弃用/Deprecated] 查询任务状态/Get task status |
| `get_user_cameo_appearances(user_id, cursor=...)` | `GET /api/v1/sora2/get_user_cameo_appearances` | 获取用户Cameo出镜秀列表/Fetch user cameo appearances |
| `get_user_followers(user_id, cursor=...)` | `GET /api/v1/sora2/get_user_followers` | 获取用户粉丝列表/Fetch user followers |
| `get_user_following(user_id, cursor=...)` | `GET /api/v1/sora2/get_user_following` | 获取用户关注列表/Fetch user following |
| `get_user_posts(user_id, cursor=...)` | `GET /api/v1/sora2/get_user_posts` | 获取用户发布的帖子列表/Fetch user posts |
| `get_user_profile(user_id)` | `GET /api/v1/sora2/get_user_profile` | 获取用户信息档案/Fetch user profile |
| `get_video_download_info(post_id=..., post_url=...)` | `GET /api/v1/sora2/get_video_download_info` | 获取无水印视频下载信息/Fetch none watermark video download info |
| `search_users(username)` | `GET /api/v1/sora2/search_users` | 搜索用户/Search users |
| `upload_image(file)` | `POST /api/v1/sora2/upload_image` | 上传图片获取media_id/Upload image to get media_id |

## `client.temp_mail`

**Class:** `tikhub.resources.temp_mail.TempMail` (sync) / `AsyncTempMail` (async)

**Endpoints:** 3

| Method | Endpoint | Summary |
|---|---|---|
| `get_email_by_id(token, message_id)` | `GET /api/v1/temp_mail/v1/get_email_by_id` | Get Email By Id |
| `get_emails_inbox(token)` | `GET /api/v1/temp_mail/v1/get_emails_inbox` | Get Emails |
| `get_temp_email_address()` | `GET /api/v1/temp_mail/v1/get_temp_email_address` | Get Temp Email |

## `client.threads_web`

**Class:** `tikhub.resources.threads_web.ThreadsWeb` (sync) / `AsyncThreadsWeb` (async)

**Endpoints:** 11

| Method | Endpoint | Summary |
|---|---|---|
| `fetch_post_comments(post_id, end_cursor=...)` | `GET /api/v1/threads/web/fetch_post_comments` | 获取帖子评论/Get post comments |
| `fetch_post_detail(post_id)` | `GET /api/v1/threads/web/fetch_post_detail` | 获取帖子详情/Get post detail |
| `fetch_post_detail_v2(post_id=..., url=...)` | `GET /api/v1/threads/web/fetch_post_detail_v2` | 获取帖子详情 V2(支持链接)/Get post detail V2(supports URL) |
| `fetch_user_info(username)` | `GET /api/v1/threads/web/fetch_user_info` | 获取用户信息/Get user info |
| `fetch_user_info_by_id(user_id)` | `GET /api/v1/threads/web/fetch_user_info_by_id` | 根据用户ID获取用户信息/Get user info by ID |
| `fetch_user_posts(user_id, end_cursor=...)` | `GET /api/v1/threads/web/fetch_user_posts` | 获取用户帖子列表/Get user posts |
| `fetch_user_replies(user_id, end_cursor=...)` | `GET /api/v1/threads/web/fetch_user_replies` | 获取用户回复列表/Get user replies |
| `fetch_user_reposts(user_id, end_cursor=...)` | `GET /api/v1/threads/web/fetch_user_reposts` | 获取用户转发列表/Get user reposts |
| `search_profiles(query)` | `GET /api/v1/threads/web/search_profiles` | 搜索用户档案/Search profiles |
| `search_recent(query, end_cursor=...)` | `GET /api/v1/threads/web/search_recent` | 搜索最新内容/Search recent content |
| `search_top(query, end_cursor=...)` | `GET /api/v1/threads/web/search_top` | 搜索热门内容/Search top content |

## `client.tikhub_downloader`

**Class:** `tikhub.resources.tikhub_downloader.TikhubDownloader` (sync) / `AsyncTikhubDownloader` (async)

**Endpoints:** 2

| Method | Endpoint | Summary |
|---|---|---|
| `redirect_download()` | `GET /api/v1/tikhub/downloader/redirect_download` | 重定向到最新版本的下载链接 / Redirect to the latest version download link |
| `version()` | `GET /api/v1/tikhub/downloader/version` | 检查TikHub下载器的版本更新 / Check for TikHub Downloader version updates |

## `client.tikhub_user`

**Class:** `tikhub.resources.tikhub_user.TikhubUser` (sync) / `AsyncTikhubUser` (async)

**Endpoints:** 6

| Method | Endpoint | Summary |
|---|---|---|
| `calculate_price(endpoint, request_per_day=...)` | `GET /api/v1/tikhub/user/calculate_price` | 计算价格/Calculate price |
| `get_all_endpoints_info()` | `GET /api/v1/tikhub/user/get_all_endpoints_info` | 获取所有端点信息/Get all endpoints information |
| `get_endpoint_info(endpoint)` | `GET /api/v1/tikhub/user/get_endpoint_info` | 获取一个端点的信息/Get information of an endpoint |
| `get_tiered_discount_info()` | `GET /api/v1/tikhub/user/get_tiered_discount_info` | 获取阶梯式折扣百分比信息/Get tiered discount percentage information |
| `get_user_daily_usage()` | `GET /api/v1/tikhub/user/get_user_daily_usage` | 获取用户每日使用情况/Get user daily usage |
| `get_user_info()` | `GET /api/v1/tikhub/user/get_user_info` | 获取TikHub用户信息/Get TikHub user info |

## `client.tiktok_ads`

**Class:** `tikhub.resources.tiktok_ads.TiktokAds` (sync) / `AsyncTiktokAds` (async)

**Endpoints:** 31

| Method | Endpoint | Summary |
|---|---|---|
| `get_ad_interactive_analysis(material_id, metric_type=..., period_type=...)` | `GET /api/v1/tiktok/ads/get_ad_interactive_analysis` | 获取广告互动分析/Get ad interactive analysis |
| `get_ad_keyframe_analysis(material_id, metric=...)` | `GET /api/v1/tiktok/ads/get_ad_keyframe_analysis` | 获取广告关键帧分析/Get ad keyframe analysis |
| `get_ad_percentile(material_id, metric=..., period_type=...)` | `GET /api/v1/tiktok/ads/get_ad_percentile` | 获取广告百分位数据/Get ad percentile data |
| `get_ads_detail(ads_id)` | `GET /api/v1/tiktok/ads/get_ads_detail` | 获取单个广告详情/Get single ad detail |
| `get_creative_patterns(first_industry_id=..., period_type=..., order_field=..., order_type=..., week=..., page=..., limit=...)` | `GET /api/v1/tiktok/ads/get_creative_patterns` | 获取创意模式排行榜/Get creative pattern rankings |
| `get_creator_filters()` | `GET /api/v1/tiktok/ads/get_creator_filters` | 获取创作者筛选器/Get creator filters |
| `get_creator_list(page=..., limit=..., sort_by=..., creator_country=..., audience_country=..., audience_count=..., keyword=...)` | `GET /api/v1/tiktok/ads/get_creator_list` | 获取创作者列表/Get creator list |
| `get_hashtag_creator(hashtag)` | `GET /api/v1/tiktok/ads/get_hashtag_creator` | 获取标签创作者信息/Get hashtag creator info |
| `get_hashtag_filters()` | `GET /api/v1/tiktok/ads/get_hashtag_filters` | 获取标签筛选器/Get hashtag filters |
| `get_hashtag_list(page=..., limit=..., period=..., country_code=..., sort_by=..., industry_id=..., filter_by=...)` | `GET /api/v1/tiktok/ads/get_hashtag_list` | 获取热门标签列表/Get popular hashtags list |
| `get_keyword_details(keyword=..., page=..., limit=..., period=..., country_code=..., order_by=..., order_type=..., industry=..., objective=..., keyword_type=...)` | `GET /api/v1/tiktok/ads/get_keyword_details` | 获取关键词详细信息/Get keyword details |
| `get_keyword_filters()` | `GET /api/v1/tiktok/ads/get_keyword_filters` | 获取关键词筛选器/Get keyword filters |
| `get_keyword_insights(page=..., limit=..., period=..., country_code=..., order_by=..., order_type=..., industry=..., objective=..., keyword_type=..., keyword=...)` | `GET /api/v1/tiktok/ads/get_keyword_insights` | 获取关键词洞察数据/Get keyword insights data |
| `get_keyword_list(keyword=..., period=..., page=..., limit=..., country_code=..., industry=...)` | `GET /api/v1/tiktok/ads/get_keyword_list` | 获取关键词列表/Get keyword list |
| `get_popular_trends(period=..., page=..., limit=..., order_by=..., country_code=...)` | `GET /api/v1/tiktok/ads/get_popular_trends` | 获取流行趋势视频/Get popular trend videos |
| `get_product_detail(id, last=..., ecom_type=..., period_type=..., country_code=...)` | `GET /api/v1/tiktok/ads/get_product_detail` | 获取产品详细信息/Get product detail |
| `get_product_filters()` | `GET /api/v1/tiktok/ads/get_product_filters` | 获取产品筛选器/Get product filters |
| `get_product_metrics(id, last=..., metrics=..., ecom_type=..., period_type=..., country_code=...)` | `GET /api/v1/tiktok/ads/get_product_metrics` | 获取产品指标数据/Get product metrics |
| `get_query_suggestions(count=..., scenario=...)` | `GET /api/v1/tiktok/ads/get_query_suggestions` | 获取查询建议/Get query suggestions |
| `get_recommended_ads(material_id, industry=..., country_code=...)` | `GET /api/v1/tiktok/ads/get_recommended_ads` | 获取推荐广告/Get recommended ads |
| `get_related_keywords(keyword=..., period=..., country_code=..., rank_type=..., content_type=..., page=..., limit=...)` | `GET /api/v1/tiktok/ads/get_related_keywords` | 获取相关关键词/Get related keywords |
| `get_sound_detail(clip_id, period=..., country_code=...)` | `GET /api/v1/tiktok/ads/get_sound_detail` | 获取音乐详情/Get sound detail |
| `get_sound_filters(rank_type=...)` | `GET /api/v1/tiktok/ads/get_sound_filters` | 获取音乐筛选器/Get sound filters |
| `get_sound_rank_list(period=..., page=..., limit=..., rank_type=..., new_on_board=..., commercial_music=..., country_code=...)` | `GET /api/v1/tiktok/ads/get_sound_rank_list` | 获取热门音乐排行榜/Get popular sound rankings |
| `get_sound_recommendations(clip_id, limit=...)` | `GET /api/v1/tiktok/ads/get_sound_recommendations` | 获取音乐推荐/Get sound recommendations |
| `get_top_ads_spotlight(industry=..., page=..., limit=...)` | `GET /api/v1/tiktok/ads/get_top_ads_spotlight` | 获取热门广告聚光灯/Get top ads spotlight |
| `get_top_products(last=..., page=..., limit=..., country_code=..., first_ecom_category_id=..., ecom_type=..., period_type=..., order_by=..., order_type=...)` | `GET /api/v1/tiktok/ads/get_top_products` | 获取热门产品列表/Get top products list |
| `search_ads(objective=..., like=..., period=..., industry=..., keyword=..., page=..., limit=..., order_by=..., country_code=..., ad_format=..., ad_language=..., search_id=...)` | `GET /api/v1/tiktok/ads/search_ads` | 搜索广告/Search ads |
| `search_creators(keyword, page=..., limit=..., sort_by=..., creator_country=...)` | `GET /api/v1/tiktok/ads/search_creators` | 搜索创作者/Search creators |
| `search_sound(keyword, period=..., page=..., limit=..., rank_type=..., new_on_board=..., commercial_music=..., country_code=...)` | `GET /api/v1/tiktok/ads/search_sound` | 搜索音乐/Search sounds |
| `search_sound_hint(keyword, period=..., page=..., limit=..., rank_type=..., country_code=..., filter_by_checked=..., commercial_music=...)` | `GET /api/v1/tiktok/ads/search_sound_hint` | 搜索音乐提示/Search sound hints |

## `client.tiktok_analytics`

**Class:** `tikhub.resources.tiktok_analytics.TiktokAnalytics` (sync) / `AsyncTiktokAnalytics` (async)

**Endpoints:** 4

| Method | Endpoint | Summary |
|---|---|---|
| `detect_fake_views(item_id, content_category=...)` | `GET /api/v1/tiktok/analytics/detect_fake_views` | 检测视频虚假流量分析/Detect fake views in video |
| `fetch_comment_keywords(item_id)` | `GET /api/v1/tiktok/analytics/fetch_comment_keywords` | 获取视频评论关键词分析/Get comment keywords analysis |
| `fetch_creator_info_and_milestones(user_id)` | `GET /api/v1/tiktok/analytics/fetch_creator_info_and_milestones` | 获取创作者信息和里程碑数据/Get creator info and milestones |
| `fetch_video_metrics(item_id)` | `GET /api/v1/tiktok/analytics/fetch_video_metrics` | 获取作品的统计数据/Get video metrics |

## `client.tiktok_app_v3`

**Class:** `tikhub.resources.tiktok_app_v3.TiktokAppV3` (sync) / `AsyncTiktokAppV3` (async)

**Endpoints:** 75

| Method | Endpoint | Summary |
|---|---|---|
| `TTencrypt_algorithm(url=..., data=..., device_info=...)` | `POST /api/v1/tiktok/app/v3/TTencrypt_algorithm` | TikTok APP加密算法/TikTok APP encryption algorithm |
| `add_video_play_count(aweme_type, item_id)` | `GET /api/v1/tiktok/app/v3/add_video_play_count` | 根据视频ID来增加作品的播放数/Increase the number of plays of the work according to the video ID |
| `check_live_room_online(room_id)` | `GET /api/v1/tiktok/app/v3/check_live_room_online` | 检测直播间是否在线/Check if live room is online |
| `check_live_room_online_batch(room_ids=...)` | `POST /api/v1/tiktok/app/v3/check_live_room_online_batch` | 批量检测直播间是否在线/Batch check if live rooms are online |
| `encrypt_decrypt_login_request(username=..., password=..., mode=...)` | `POST /api/v1/tiktok/app/v3/encrypt_decrypt_login_request` | 加密或解密 TikTok APP 登录请求体/Encrypt or Decrypt TikTok APP login request body |
| `fetch_content_translate(trg_lang=..., src_content=...)` | `POST /api/v1/tiktok/app/v3/fetch_content_translate` | 获取内容翻译数据/Get content translation data |
| `fetch_creator_info(creator_uid)` | `GET /api/v1/tiktok/app/v3/fetch_creator_info` | 获取带货创作者信息/Get shopping creator information |
| `fetch_creator_search_insights(offset=..., limit=..., tab=..., language_filters=..., category_filters=..., creator_source=..., force_refresh=...)` | `GET /api/v1/tiktok/app/v3/fetch_creator_search_insights` | 创作者搜索洞察/Creator Search Insights |
| `fetch_creator_search_insights_detail(query_id_str, time_range=..., start_date=..., end_date=..., dimension_list=...)` | `GET /api/v1/tiktok/app/v3/fetch_creator_search_insights_detail` | 创作者搜索洞察详情/Creator Search Insights Detail |
| `fetch_creator_search_insights_trend(query_id_str, from_tab_path=..., query_analysis_required=...)` | `GET /api/v1/tiktok/app/v3/fetch_creator_search_insights_trend` | 创作者搜索洞察趋势/Creator Search Insights Trend |
| `fetch_creator_search_insights_videos(keyword, offset=..., count=...)` | `GET /api/v1/tiktok/app/v3/fetch_creator_search_insights_videos` | 创作者搜索洞察相关视频/Creator Search Insights Videos |
| `fetch_creator_showcase_product_list(kol_id, count=..., next_scroll_param=...)` | `GET /api/v1/tiktok/app/v3/fetch_creator_showcase_product_list` | 获取创作者橱窗商品列表/Get creator showcase product list |
| `fetch_general_search_result(keyword, offset=..., count=..., sort_type=..., publish_time=...)` | `GET /api/v1/tiktok/app/v3/fetch_general_search_result` | 获取指定关键词的综合搜索结果/Get comprehensive search results of specified keywords |
| `fetch_hashtag_detail(ch_id)` | `GET /api/v1/tiktok/app/v3/fetch_hashtag_detail` | 获取指定话题的详情数据/Get details of specified hashtag |
| `fetch_hashtag_search_result(keyword, offset=..., count=...)` | `GET /api/v1/tiktok/app/v3/fetch_hashtag_search_result` | 获取指定关键词的话题搜索结果/Get hashtag search results of specified keywords |
| `fetch_hashtag_video_list(ch_id, cursor=..., count=...)` | `GET /api/v1/tiktok/app/v3/fetch_hashtag_video_list` | 获取指定话题的作品数据/Get video list of specified hashtag |
| `fetch_home_feed(cookie=...)` | `POST /api/v1/tiktok/app/v3/fetch_home_feed` | 获取主页视频推荐数据/Get home feed(recommend) video data |
| `fetch_live_daily_rank(anchor_id=..., room_id=..., rank_type=..., region_type=..., gap_interval=..., cookie=...)` | `GET /api/v1/tiktok/app/v3/fetch_live_daily_rank` | 获取直播每日榜单数据/Get live daily rank data |
| `fetch_live_ranking_list(room_id, anchor_id)` | `GET /api/v1/tiktok/app/v3/fetch_live_ranking_list` | 获取直播间排行榜数据/Get live room ranking list |
| `fetch_live_room_info(room_id)` | `GET /api/v1/tiktok/app/v3/fetch_live_room_info` | 获取指定直播间的数据/Get data of specified live room |
| `fetch_live_room_product_list(room_id, author_id, page_size=..., offset=..., region=..., cookie=...)` | `GET /api/v1/tiktok/app/v3/fetch_live_room_product_list` | 获取直播间商品列表数据/Get live room product list data |
| `fetch_live_room_product_list_v2(room_id, author_id, page_size=..., offset=..., region=..., cookie=...)` | `GET /api/v1/tiktok/app/v3/fetch_live_room_product_list_v2` | 获取直播间商品列表数据 V2 /Get live room product list data V2 |
| `fetch_live_search_result(keyword, offset=..., count=..., region=...)` | `GET /api/v1/tiktok/app/v3/fetch_live_search_result` | 获取指定关键词的直播搜索结果/Get live search results of specified keywords |
| `fetch_location_search(keyword, offset=..., count=...)` | `GET /api/v1/tiktok/app/v3/fetch_location_search` | 获取地点搜索结果/Get location search results |
| `fetch_multi_video(body)` | `POST /api/v1/tiktok/app/v3/fetch_multi_video` | 批量获取视频信息/Batch Get Video Information |
| `fetch_multi_video_v2(body)` | `POST /api/v1/tiktok/app/v3/fetch_multi_video_v2` | 批量获取视频信息 V2/Batch Get Video Information V2 |
| `fetch_music_chart_list(scene=..., cursor=..., count=...)` | `GET /api/v1/tiktok/app/v3/fetch_music_chart_list` | 音乐排行榜/Music Chart List |
| `fetch_music_detail(music_id)` | `GET /api/v1/tiktok/app/v3/fetch_music_detail` | 获取指定音乐的详情数据/Get details of specified music |
| `fetch_music_search_result(keyword, offset=..., count=..., filter_by=..., sort_type=..., region=...)` | `GET /api/v1/tiktok/app/v3/fetch_music_search_result` | 获取指定关键词的音乐搜索结果/Get music search results of specified keywords |
| `fetch_music_video_list(music_id, cursor=..., count=...)` | `GET /api/v1/tiktok/app/v3/fetch_music_video_list` | 获取指定音乐的视频列表数据/Get video list of specified music |
| `fetch_one_video(aweme_id)` | `GET /api/v1/tiktok/app/v3/fetch_one_video` | 获取单个作品数据/Get single video data |
| `fetch_one_video_by_share_url(share_url)` | `GET /api/v1/tiktok/app/v3/fetch_one_video_by_share_url` | 根据分享链接获取单个作品数据/Get single video data by sharing link |
| `fetch_one_video_by_share_url_v2(share_url)` | `GET /api/v1/tiktok/app/v3/fetch_one_video_by_share_url_v2` | 根据分享链接获取单个作品数据/Get single video data by sharing link |
| `fetch_one_video_v2(aweme_id)` | `GET /api/v1/tiktok/app/v3/fetch_one_video_v2` | 获取单个作品数据 V2/Get single video data V2 |
| `fetch_one_video_v3(aweme_id, region=...)` | `GET /api/v1/tiktok/app/v3/fetch_one_video_v3` | 获取单个作品数据 V3(支持国家参数)/Get single video data V3 (support country parameter) |
| `fetch_product_detail(product_id)` | `GET /api/v1/tiktok/app/v3/fetch_product_detail` | 获取商品详情数据（即将弃用，使用 fetch_product_detail_v2 代替）/Get product detail data (will be deprecated, use fetch_product_detail_v2 in |
| `fetch_product_detail_v2(product_id)` | `GET /api/v1/tiktok/app/v3/fetch_product_detail_v2` | 获取商品详情数据V2/Get product detail data V2 |
| `fetch_product_detail_v3(product_id, region=...)` | `GET /api/v1/tiktok/app/v3/fetch_product_detail_v3` | 获取商品详情数据V3 / Get product detail data V3 |
| `fetch_product_detail_v4(product_id, region=...)` | `GET /api/v1/tiktok/app/v3/fetch_product_detail_v4` | 获取商品详情数据V4 / Get product detail data V4 |
| `fetch_product_id_by_share_link(share_link)` | `GET /api/v1/tiktok/app/v3/fetch_product_id_by_share_link` | 通过分享链接获取商品ID/Get Product ID by Share Link |
| `fetch_product_review(product_id, cursor=..., size=..., filter_id=..., sort_type=...)` | `GET /api/v1/tiktok/app/v3/fetch_product_review` | 获取商品评价数据/Get product review data |
| `fetch_product_search(keyword, cursor=..., count=..., sort_type=..., customer_review_four_star=..., have_discount=..., min_price=..., max_price=...)` | `GET /api/v1/tiktok/app/v3/fetch_product_search` | 获取商品搜索结果/Get product search results |
| `fetch_share_qr_code(object_id, schema_type=...)` | `GET /api/v1/tiktok/app/v3/fetch_share_qr_code` | 获取分享二维码/Get share QR code |
| `fetch_share_short_link(url)` | `GET /api/v1/tiktok/app/v3/fetch_share_short_link` | 获取分享短链接/Get share short link |
| `fetch_shop_home(page_id, seller_id)` | `GET /api/v1/tiktok/app/v3/fetch_shop_home` | 获取商家主页数据/Get shop home page data |
| `fetch_shop_home_page_list(seller_id)` | `GET /api/v1/tiktok/app/v3/fetch_shop_home_page_list` | 获取商家主页Page列表数据/Get shop home page list data |
| `fetch_shop_id_by_share_link(share_link)` | `GET /api/v1/tiktok/app/v3/fetch_shop_id_by_share_link` | 通过分享链接获取店铺ID/Get Shop ID by Share Link |
| `fetch_shop_info(shop_id)` | `GET /api/v1/tiktok/app/v3/fetch_shop_info` | 获取商家信息数据/Get shop information data |
| `fetch_shop_product_category(seller_id)` | `GET /api/v1/tiktok/app/v3/fetch_shop_product_category` | 获取商家产品分类数据/Get shop product category data |
| `fetch_shop_product_list(seller_id, scroll_params=..., page_size=..., sort_field=..., sort_order=...)` | `GET /api/v1/tiktok/app/v3/fetch_shop_product_list` | 获取商家商品列表数据/Get shop product list data |
| `fetch_shop_product_list_v2(seller_id, scroll_params=..., page_size=..., sort_field=..., sort_order=...)` | `GET /api/v1/tiktok/app/v3/fetch_shop_product_list_v2` | 获取商家商品列表数据 V2/Get shop product list data V2 |
| `fetch_shop_product_recommend(seller_id, scroll_param=..., page_size=...)` | `GET /api/v1/tiktok/app/v3/fetch_shop_product_recommend` | 获取商家商品推荐数据/Get shop product recommend data |
| `fetch_similar_user_recommendations(sec_uid, page_token=...)` | `GET /api/v1/tiktok/app/v3/fetch_similar_user_recommendations` | 获取类似用户推荐/Similar User Recommendations |
| `fetch_user_country_by_username(username)` | `GET /api/v1/tiktok/app/v3/fetch_user_country_by_username` | 通过用户名获取用户账号国家地区/Get user account country by username |
| `fetch_user_follower_list(user_id=..., sec_user_id=..., count=..., min_time=..., page_token=...)` | `GET /api/v1/tiktok/app/v3/fetch_user_follower_list` | 获取指定用户的粉丝列表数据/Get follower list of specified user |
| `fetch_user_following_list(user_id=..., sec_user_id=..., count=..., min_time=..., page_token=...)` | `GET /api/v1/tiktok/app/v3/fetch_user_following_list` | 获取指定用户的关注列表数据/Get following list of specified user |
| `fetch_user_like_videos(sec_user_id, max_cursor=..., counts=...)` | `GET /api/v1/tiktok/app/v3/fetch_user_like_videos` | 获取用户喜欢作品数据/Get user like video data |
| `fetch_user_music_list(sec_uid, cursor=..., count=...)` | `GET /api/v1/tiktok/app/v3/fetch_user_music_list` | 获取用户音乐列表数据/Get user music list data |
| `fetch_user_post_videos(sec_user_id=..., unique_id=..., max_cursor=..., count=..., sort_type=...)` | `GET /api/v1/tiktok/app/v3/fetch_user_post_videos` | 获取用户主页作品数据 V1/Get user homepage video data V1 |
| `fetch_user_post_videos_v2(sec_user_id=..., unique_id=..., max_cursor=..., count=..., sort_type=...)` | `GET /api/v1/tiktok/app/v3/fetch_user_post_videos_v2` | 获取用户主页作品数据 V2/Get user homepage video data V2 |
| `fetch_user_post_videos_v3(sec_user_id=..., unique_id=..., max_cursor=..., count=..., sort_type=...)` | `GET /api/v1/tiktok/app/v3/fetch_user_post_videos_v3` | 获取用户主页作品数据 V3（精简数据-更快速）/Get user homepage video data V3 (simplified data - faster) |
| `fetch_user_repost_videos(user_id, offset=..., count=...)` | `GET /api/v1/tiktok/app/v3/fetch_user_repost_videos` | 获取用户转发的作品数据/Get user repost video data |
| `fetch_user_search_result(keyword, offset=..., count=..., user_search_follower_count=..., user_search_profile_type=..., user_search_other_pref=...)` | `GET /api/v1/tiktok/app/v3/fetch_user_search_result` | 获取指定关键词的用户搜索结果/Get user search results of specified keywords |
| `fetch_video_comment_replies(item_id, comment_id, cursor=..., count=...)` | `GET /api/v1/tiktok/app/v3/fetch_video_comment_replies` | 获取指定视频的评论回复数据/Get comment replies data of specified video |
| `fetch_video_comments(aweme_id, cursor=..., count=...)` | `GET /api/v1/tiktok/app/v3/fetch_video_comments` | 获取单个视频评论数据/Get single video comments data |
| `fetch_video_search_result(keyword, offset=..., count=..., sort_type=..., publish_time=..., region=...)` | `GET /api/v1/tiktok/app/v3/fetch_video_search_result` | 获取指定关键词的视频搜索结果/Get video search results of specified keywords |
| `fetch_webcast_user_info(user_id=..., sec_user_id=...)` | `GET /api/v1/tiktok/app/v3/fetch_webcast_user_info` | 获取指定 Webcast 用户的信息/Get information of specified Webcast user |
| `get_user_id_and_sec_user_id_by_username(username)` | `GET /api/v1/tiktok/app/v3/get_user_id_and_sec_user_id_by_username` | 使用用户名获取用户 user_id 和 sec_user_id/Get user_id and sec_user_id by Username |
| `handler_user_profile(user_id=..., sec_user_id=..., unique_id=...)` | `GET /api/v1/tiktok/app/v3/handler_user_profile` | 获取指定用户的信息/Get information of specified user |
| `open_tiktok_app_to_keyword_search(keyword)` | `GET /api/v1/tiktok/app/v3/open_tiktok_app_to_keyword_search` | 生成TikTok分享链接，唤起TikTok APP，跳转指定关键词搜索结果/Generate TikTok share link, call TikTok APP, and jump to the specified keyword sea |
| `open_tiktok_app_to_send_private_message(uid)` | `GET /api/v1/tiktok/app/v3/open_tiktok_app_to_send_private_message` | 生成TikTok分享链接，唤起TikTok APP，给指定用户发送私信/Generate TikTok share link, call TikTok APP, and send private messages to specified  |
| `open_tiktok_app_to_user_profile(uid)` | `GET /api/v1/tiktok/app/v3/open_tiktok_app_to_user_profile` | 生成TikTok分享链接，唤起TikTok APP，跳转指定用户主页/Generate TikTok share link, call TikTok APP, and jump to the specified user profile |
| `open_tiktok_app_to_video_detail(aweme_id)` | `GET /api/v1/tiktok/app/v3/open_tiktok_app_to_video_detail` | 生成TikTok分享链接，唤起TikTok APP，跳转指定作品详情页/Generate TikTok share link, call TikTok APP, and jump to the specified video details |
| `search_follower_list(user_id, keyword)` | `GET /api/v1/tiktok/app/v3/search_follower_list` | 搜索粉丝列表/Search follower list |
| `search_following_list(user_id, keyword)` | `GET /api/v1/tiktok/app/v3/search_following_list` | 搜索关注列表/Search following list |

## `client.tiktok_creator`

**Class:** `tikhub.resources.tiktok_creator.TiktokCreator` (sync) / `AsyncTiktokCreator` (async)

**Endpoints:** 14

| Method | Endpoint | Summary |
|---|---|---|
| `get_account_health_status(cookie=..., proxy=...)` | `POST /api/v1/tiktok/creator/get_account_health_status` | 获取创作者账号健康状态/Get Creator Account Health Status |
| `get_account_insights_overview(cookie=..., proxy=..., start_date=...)` | `POST /api/v1/tiktok/creator/get_account_insights_overview` | 获取创作者账号概览/Get Creator Account Overview |
| `get_account_violation_list(cookie=..., proxy=..., page=...)` | `POST /api/v1/tiktok/creator/get_account_violation_list` | 获取创作者账号违规记录列表/Get Creator Account Violation Record List |
| `get_creator_account_info(cookie=..., proxy=...)` | `POST /api/v1/tiktok/creator/get_creator_account_info` | 获取创作者账号信息/Get Creator Account Info |
| `get_live_analytics_summary(cookie=..., proxy=..., start_date=...)` | `POST /api/v1/tiktok/creator/get_live_analytics_summary` | 获取创作者直播概览/Get Creator Live Overview |
| `get_product_analytics_list(cookie=..., proxy=..., start_date=..., end_date=..., page=...)` | `POST /api/v1/tiktok/creator/get_product_analytics_list` | 获取创作者商品列表分析/Get Creator Product List Analytics |
| `get_product_related_videos(item_id, product_id, cookie=..., proxy=..., start_date=...)` | `POST /api/v1/tiktok/creator/get_product_related_videos` | 获取同款商品关联视频/Get Product Related Videos |
| `get_showcase_product_list(cookie=..., proxy=..., count=..., offset=...)` | `POST /api/v1/tiktok/creator/get_showcase_product_list` | 获取橱窗商品列表/Get Showcase Product List |
| `get_video_analytics_summary(cookie=..., proxy=...)` | `POST /api/v1/tiktok/creator/get_video_analytics_summary` | 获取创作者视频概览/Get Creator Video Overview |
| `get_video_associated_product_list(item_ids, cookie=..., proxy=..., start_date=...)` | `POST /api/v1/tiktok/creator/get_video_associated_product_list` | 获取视频关联商品列表/Get Video Associated Product List |
| `get_video_audience_stats(item_id, cookie=..., proxy=..., start_date=...)` | `POST /api/v1/tiktok/creator/get_video_audience_stats` | 获取视频受众分析数据/Get Video Audience Analysis Data |
| `get_video_detailed_stats(item_id, cookie=..., proxy=..., start_date=...)` | `POST /api/v1/tiktok/creator/get_video_detailed_stats` | 获取视频详细分段统计数据/Get Video Detailed Statistics |
| `get_video_list_analytics(cookie=..., proxy=..., start_date=..., page=..., rules=...)` | `POST /api/v1/tiktok/creator/get_video_list_analytics` | 获取创作者视频列表分析/Get Creator Video List Analytics |
| `get_video_to_product_stats(item_id, product_id, cookie=..., proxy=..., start_date=...)` | `POST /api/v1/tiktok/creator/get_video_to_product_stats` | 获取视频与商品关联统计数据/Get Video-Product Association Statistics |

## `client.tiktok_interaction`

**Class:** `tikhub.resources.tiktok_interaction.TiktokInteraction` (sync) / `AsyncTiktokInteraction` (async)

**Endpoints:** 7

| Method | Endpoint | Summary |
|---|---|---|
| `apply(api_key, invite_code)` | `GET /api/v1/tiktok/interaction/apply` | 申请使用TikTok交互API权限（Scope）/Apply for TikTok Interaction API permission (Scope) |
| `collect(aweme_id=..., cookie=..., device_id=..., iid=..., proxy=...)` | `POST /api/v1/tiktok/interaction/collect` | 收藏/Collect |
| `follow(user_id=..., sec_user_id=..., cookie=..., device_id=..., iid=..., proxy=...)` | `POST /api/v1/tiktok/interaction/follow` | 关注/Follow |
| `forward(aweme_id=..., cookie=..., device_id=..., iid=..., proxy=...)` | `POST /api/v1/tiktok/interaction/forward` | 转发/Forward |
| `like(aweme_id=..., cookie=..., device_id=..., iid=..., proxy=...)` | `POST /api/v1/tiktok/interaction/like` | 点赞/Like |
| `post_comment(aweme_id=..., text=..., cookie=..., device_id=..., iid=..., proxy=...)` | `POST /api/v1/tiktok/interaction/post_comment` | 发送评论/Post comment |
| `reply_comment(aweme_id=..., reply_id=..., text=..., cookie=..., device_id=..., iid=..., proxy=...)` | `POST /api/v1/tiktok/interaction/reply_comment` | 回复评论/Reply to comment |

## `client.tiktok_shop_web`

**Class:** `tikhub.resources.tiktok_shop_web.TiktokShopWeb` (sync) / `AsyncTiktokShopWeb` (async)

**Endpoints:** 15

| Method | Endpoint | Summary |
|---|---|---|
| `fetch_hot_selling_products_list(region=..., count=...)` | `GET /api/v1/tiktok/shop/web/fetch_hot_selling_products_list` | 获取热卖商品列表/Get hot selling products list |
| `fetch_product_detail(product_id, seller_id=..., region=...)` | `GET /api/v1/tiktok/shop/web/fetch_product_detail` | 获取商品详情V1(桌面端-数据完整)/Get product detail V1(Full data) |
| `fetch_product_detail_v2(product_id, seller_id=..., region=...)` | `GET /api/v1/tiktok/shop/web/fetch_product_detail_v2` | 获取商品详情V2(移动端-数据少)/Get product detail V2 (Less Data) |
| `fetch_product_detail_v3(product_id, region=...)` | `GET /api/v1/tiktok/shop/web/fetch_product_detail_v3` | 获取商品详情V3(移动端-数据完整)/Get product detail V3 (Full Data) |
| `fetch_product_reviews_v1(product_id, sort_type=..., filter_id=..., offset=...)` | `GET /api/v1/tiktok/shop/web/fetch_product_reviews_v1` | 获取商品评论V1/Get product reviews V1 |
| `fetch_product_reviews_v2(product_id, page_start=..., sort_rule=..., filter_type=..., filter_value=..., region=...)` | `GET /api/v1/tiktok/shop/web/fetch_product_reviews_v2` | 获取商品评论V2/Get product reviews V2 |
| `fetch_products_by_category_id(category_id, offset=..., region=...)` | `GET /api/v1/tiktok/shop/web/fetch_products_by_category_id` | 根据分类ID获取商品列表/Get products by category ID |
| `fetch_products_category_list(region=...)` | `GET /api/v1/tiktok/shop/web/fetch_products_category_list` | 获取商品分类列表/Get product category list |
| `fetch_search_products_list(search_word, offset=..., page_token=..., region=...)` | `GET /api/v1/tiktok/shop/web/fetch_search_products_list` | 搜索商品列表V1/Search products list V1 |
| `fetch_search_products_list_v2(search_word, offset=..., page_token=..., region=...)` | `GET /api/v1/tiktok/shop/web/fetch_search_products_list_v2` | 搜索商品列表V2(移动端)/Search products list V2 (Mobile) |
| `fetch_search_products_list_v3(keyword, offset=..., region=..., sort_by=..., filters_data=...)` | `GET /api/v1/tiktok/shop/web/fetch_search_products_list_v3` | 搜索商品列表V3/Search products list V3 |
| `fetch_search_word_suggestion(search_word, lang=..., region=...)` | `GET /api/v1/tiktok/shop/web/fetch_search_word_suggestion` | 获取搜索关键词建议V1/Get search keyword suggestions V1 |
| `fetch_search_word_suggestion_v2(search_word, lang=..., region=...)` | `GET /api/v1/tiktok/shop/web/fetch_search_word_suggestion_v2` | 获取搜索关键词建议V2(移动端)/Get search keyword suggestions V2 (Mobile) |
| `fetch_seller_products_list(seller_id, search_params=..., region=...)` | `GET /api/v1/tiktok/shop/web/fetch_seller_products_list` | 获取商家商品列表V1/Get seller products list V1 |
| `fetch_seller_products_list_v2(seller_id, searchParams=..., region=...)` | `GET /api/v1/tiktok/shop/web/fetch_seller_products_list_v2` | 获取商家商品列表V2(移动端)/Get seller products list V2 (Mobile) |

## `client.tiktok_web`

**Class:** `tikhub.resources.tiktok_web.TiktokWeb` (sync) / `AsyncTiktokWeb` (async)

**Endpoints:** 59

| Method | Endpoint | Summary |
|---|---|---|
| `decrypt_strData(encrypted_data)` | `GET /api/v1/tiktok/web/decrypt_strData` | 解密strData/Decrypt strData |
| `device_register()` | `GET /api/v1/tiktok/web/device_register` | 设备注册/Register device for TikTok Web |
| `encrypt_strData(data)` | `GET /api/v1/tiktok/web/encrypt_strData` | 加密strData/Encrypt strData |
| `fetch_batch_check_live_alive(room_ids)` | `GET /api/v1/tiktok/web/fetch_batch_check_live_alive` | 批量直播间开播状态检测/Batch live room start status check |
| `fetch_check_live_alive(room_id)` | `GET /api/v1/tiktok/web/fetch_check_live_alive` | 直播间开播状态检测/Live room start status check |
| `fetch_explore_post(categoryType=..., count=...)` | `GET /api/v1/tiktok/web/fetch_explore_post` | 获取探索作品数据/Get explore video data |
| `fetch_general_search(keyword, offset=..., search_id=..., cookie=...)` | `GET /api/v1/tiktok/web/fetch_general_search` | 获取综合搜索列表/Get general search list |
| `fetch_gift_name_by_id(gift_id)` | `POST /api/v1/tiktok/web/fetch_gift_name_by_id` | 根据Gift ID查询礼物名称/Get gift name by gift ID |
| `fetch_gift_names_by_ids(gift_ids)` | `POST /api/v1/tiktok/web/fetch_gift_names_by_ids` | 批量查询Gift ID对应的礼物名称($0.025/次,建议50个)/Batch get gift names by gift IDs ($0.025/call, suggest 50) |
| `fetch_home_feed(count=..., cookie=...)` | `POST /api/v1/tiktok/web/fetch_home_feed` | 首页推荐作品/Home Feed |
| `fetch_live_gift_list(room_id=...)` | `GET /api/v1/tiktok/web/fetch_live_gift_list` | 获取直播间礼物列表/Get live room gift list |
| `fetch_live_im_fetch(room_id, user_unique_id)` | `GET /api/v1/tiktok/web/fetch_live_im_fetch` | TikTok直播间弹幕参数获取/tiktok live room danmaku parameters |
| `fetch_live_recommend(related_live_tag)` | `GET /api/v1/tiktok/web/fetch_live_recommend` | 获取直播间首页推荐列表/Get live room homepage recommendation list |
| `fetch_post_comment(aweme_id, cursor=..., count=..., current_region=...)` | `GET /api/v1/tiktok/web/fetch_post_comment` | 获取作品的评论列表/Get video comments |
| `fetch_post_comment_reply(item_id, comment_id, cursor=..., count=..., current_region=...)` | `GET /api/v1/tiktok/web/fetch_post_comment_reply` | 获取作品的评论回复列表/Get video comment replies |
| `fetch_post_detail(itemId)` | `GET /api/v1/tiktok/web/fetch_post_detail` | 获取单个作品数据/Get single video data |
| `fetch_post_detail_v2(itemId)` | `GET /api/v1/tiktok/web/fetch_post_detail_v2` | 获取单个作品数据 V2/Get single video data V2 |
| `fetch_search_keyword_suggest(keyword)` | `GET /api/v1/tiktok/web/fetch_search_keyword_suggest` | 搜索关键字推荐/Search keyword suggest |
| `fetch_search_live(keyword, count=..., offset=..., search_id=..., cookie=...)` | `GET /api/v1/tiktok/web/fetch_search_live` | 搜索直播/Search live |
| `fetch_search_photo(keyword, count=..., offset=..., search_id=..., cookie=...)` | `GET /api/v1/tiktok/web/fetch_search_photo` | 搜索照片/Search photo |
| `fetch_search_user(keyword, cursor=..., search_id=..., cookie=...)` | `GET /api/v1/tiktok/web/fetch_search_user` | 搜索用户/Search user |
| `fetch_search_video(keyword, count=..., offset=..., search_id=..., cookie=...)` | `GET /api/v1/tiktok/web/fetch_search_video` | 搜索视频/Search video |
| `fetch_sso_login_auth(device_id, verifyFp, region, proxy)` | `GET /api/v1/tiktok/web/fetch_sso_login_auth` | 认证SSO登录/Authenticate SSO login |
| `fetch_sso_login_qrcode(device_id, region, proxy)` | `GET /api/v1/tiktok/web/fetch_sso_login_qrcode` | 获取SSO登录二维码/Get SSO login QR code |
| `fetch_sso_login_status(token, device_id, verifyFp, region, proxy)` | `GET /api/v1/tiktok/web/fetch_sso_login_status` | 获取SSO登录状态/Get SSO login status |
| `fetch_tag_detail(tag_name)` | `GET /api/v1/tiktok/web/fetch_tag_detail` | Tag详情/Tag Detail |
| `fetch_tag_post(challengeID, count=..., cursor=...)` | `GET /api/v1/tiktok/web/fetch_tag_post` | Tag作品/Tag Post |
| `fetch_tiktok_live_data(live_room_url)` | `GET /api/v1/tiktok/web/fetch_tiktok_live_data` | 通过直播链接获取直播间信息/Get live room information via live link |
| `fetch_tiktok_web_guest_cookie(user_agent)` | `GET /api/v1/tiktok/web/fetch_tiktok_web_guest_cookie` | 获取游客 Cookie/Get the guest Cookie |
| `fetch_trending_post()` | `GET /api/v1/tiktok/web/fetch_trending_post` | 获取每日热门内容作品数据/Get daily trending video data |
| `fetch_trending_searchwords()` | `GET /api/v1/tiktok/web/fetch_trending_searchwords` | 获取每日趋势搜索关键词/Get daily trending search words |
| `fetch_user_collect(cookie, secUid, cursor=..., count=..., coverFormat=...)` | `GET /api/v1/tiktok/web/fetch_user_collect` | 获取用户的收藏列表/Get user favorites |
| `fetch_user_fans(secUid, count=..., maxCursor=..., minCursor=...)` | `GET /api/v1/tiktok/web/fetch_user_fans` | 获取用户的粉丝列表/Get user followers |
| `fetch_user_follow(secUid, count=..., maxCursor=..., minCursor=...)` | `GET /api/v1/tiktok/web/fetch_user_follow` | 获取用户的关注列表/Get user followings |
| `fetch_user_like(secUid, cursor=..., count=..., coverFormat=..., post_item_list_request_type=...)` | `GET /api/v1/tiktok/web/fetch_user_like` | 获取用户的点赞列表/Get user likes |
| `fetch_user_live_detail(uniqueId)` | `GET /api/v1/tiktok/web/fetch_user_live_detail` | 获取用户的直播详情/Get user live details |
| `fetch_user_mix(mixId, cursor=..., count=...)` | `GET /api/v1/tiktok/web/fetch_user_mix` | 获取用户的合辑列表/Get user mix list |
| `fetch_user_play_list(secUid, cursor=..., count=...)` | `GET /api/v1/tiktok/web/fetch_user_play_list` | 获取用户的播放列表/Get user play list |
| `fetch_user_post(secUid, cursor=..., count=..., coverFormat=..., post_item_list_request_type=...)` | `GET /api/v1/tiktok/web/fetch_user_post` | 获取用户的作品列表/Get user posts |
| `fetch_user_profile(uniqueId=..., secUid=...)` | `GET /api/v1/tiktok/web/fetch_user_profile` | 获取用户的个人信息/Get user profile |
| `fetch_user_repost(secUid, cursor=..., count=..., coverFormat=...)` | `GET /api/v1/tiktok/web/fetch_user_repost` | 获取用户的转发作品列表/Get user reposts |
| `generate_fingerprint(browser_type=...)` | `GET /api/v1/tiktok/web/generate_fingerprint` | 生成浏览器指纹/Generate browser fingerprint |
| `generate_hashed_id(email)` | `GET /api/v1/tiktok/web/generate_hashed_id` | 生成哈希ID/Generate hashed ID |
| `generate_real_msToken(random_strData=..., browser_type=...)` | `GET /api/v1/tiktok/web/generate_real_msToken` | 生成真实msToken/Generate real msToken |
| `generate_ttwid(user_agent=...)` | `GET /api/v1/tiktok/web/generate_ttwid` | 生成ttwid/Generate ttwid |
| `generate_webid(cookie=..., user_agent=..., url=..., referer=..., user_unique_id=..., app_id=...)` | `GET /api/v1/tiktok/web/generate_webid` | 生成web_id/Generate web_id |
| `generate_x_mssdk_info(user_agent=...)` | `POST /api/v1/tiktok/web/generate_x_mssdk_info` | 生成 X-Mssdk-Info /Generate X-Mssdk-Info |
| `generate_xbogus(url, user_agent)` | `POST /api/v1/tiktok/web/generate_xbogus` | 生成 XBogus/Generate XBogus |
| `generate_xgnarly(url, body=...)` | `POST /api/v1/tiktok/web/generate_xgnarly` | 生成 XGnarly /Generate XGnarly |
| `generate_xgnarly_and_xbogus(url, body=...)` | `POST /api/v1/tiktok/web/generate_xgnarly_and_xbogus` | 生成 XGnarly 和 XBogus /Generate XGnarly and XBogus |
| `get_all_aweme_id(body)` | `POST /api/v1/tiktok/web/get_all_aweme_id` | 提取列表作品id/Extract list video id |
| `get_all_sec_user_id(body)` | `POST /api/v1/tiktok/web/get_all_sec_user_id` | 提取列表用户sec_user_id/Extract list user sec_user_id |
| `get_all_unique_id(body)` | `POST /api/v1/tiktok/web/get_all_unique_id` | 获取列表unique_id/Get list unique_id |
| `get_aweme_id(url)` | `GET /api/v1/tiktok/web/get_aweme_id` | 提取单个作品id/Extract single video id |
| `get_live_room_id(live_room_url)` | `GET /api/v1/tiktok/web/get_live_room_id` | 根据直播间链接提取直播间ID/Extract live room ID from live room link |
| `get_sec_user_id(url)` | `GET /api/v1/tiktok/web/get_sec_user_id` | 提取用户sec_user_id/Extract user sec_user_id |
| `get_unique_id(url)` | `GET /api/v1/tiktok/web/get_unique_id` | 获取用户unique_id/Get user unique_id |
| `get_user_id(url)` | `GET /api/v1/tiktok/web/get_user_id` | 提取用户user_id/Extract user user_id |
| `tiktok_live_room(live_room_url, danmaku_type)` | `GET /api/v1/tiktok/web/tiktok_live_room` | 提取直播间弹幕/Extract live room danmaku |

## `client.toutiao_app`

**Class:** `tikhub.resources.toutiao_app.ToutiaoApp` (sync) / `AsyncToutiaoApp` (async)

**Endpoints:** 5

| Method | Endpoint | Summary |
|---|---|---|
| `get_article_info(group_id)` | `GET /api/v1/toutiao/app/get_article_info` | 获取指定文章的信息/Get information of specified article |
| `get_comments(group_id, offset)` | `GET /api/v1/toutiao/app/get_comments` | 获取指定作品的评论/Get comments of specified post |
| `get_user_id(user_profile_url)` | `GET /api/v1/toutiao/app/get_user_id` | 从头条用户主页获取用户user_id/Get user_id from user profile |
| `get_user_info(user_id)` | `GET /api/v1/toutiao/app/get_user_info` | 获取指定用户的信息/Get information of specified user |
| `get_video_info(group_id)` | `GET /api/v1/toutiao/app/get_video_info` | 获取指定视频的信息/Get information of specified video |

## `client.toutiao_web`

**Class:** `tikhub.resources.toutiao_web.ToutiaoWeb` (sync) / `AsyncToutiaoWeb` (async)

**Endpoints:** 2

| Method | Endpoint | Summary |
|---|---|---|
| `get_article_info(aweme_id)` | `GET /api/v1/toutiao/web/get_article_info` | 获取指定文章的信息/Get information of specified article |
| `get_video_info(aweme_id)` | `GET /api/v1/toutiao/web/get_video_info` | 获取指定视频的信息/Get information of specified video |

## `client.twitter_web`

**Class:** `tikhub.resources.twitter_web.TwitterWeb` (sync) / `AsyncTwitterWeb` (async)

**Endpoints:** 13

| Method | Endpoint | Summary |
|---|---|---|
| `fetch_latest_post_comments(tweet_id, cursor=...)` | `GET /api/v1/twitter/web/fetch_latest_post_comments` | 获取最新的推文评论/Get the latest tweet comments |
| `fetch_post_comments(tweet_id, cursor=...)` | `GET /api/v1/twitter/web/fetch_post_comments` | 获取评论/Get comments |
| `fetch_retweet_user_list(tweet_id, cursor=...)` | `GET /api/v1/twitter/web/fetch_retweet_user_list` | 转推用户列表/ReTweet User list |
| `fetch_search_timeline(keyword, search_type=..., cursor=...)` | `GET /api/v1/twitter/web/fetch_search_timeline` | 搜索/Search |
| `fetch_trending(country=...)` | `GET /api/v1/twitter/web/fetch_trending` | 趋势/Trending |
| `fetch_tweet_detail(tweet_id)` | `GET /api/v1/twitter/web/fetch_tweet_detail` | 获取单个推文数据/Get single tweet data |
| `fetch_user_followers(screen_name, cursor=...)` | `GET /api/v1/twitter/web/fetch_user_followers` | 用户粉丝/User Followers |
| `fetch_user_followings(screen_name, cursor=...)` | `GET /api/v1/twitter/web/fetch_user_followings` | 用户关注/User Followings |
| `fetch_user_highlights_tweets(userId, count=..., cursor=...)` | `GET /api/v1/twitter/web/fetch_user_highlights_tweets` | 获取用户高光推文/Get user highlights tweets |
| `fetch_user_media(screen_name, rest_id=..., cursor=...)` | `GET /api/v1/twitter/web/fetch_user_media` | 获取用户媒体/Get user media |
| `fetch_user_post_tweet(screen_name=..., rest_id=..., cursor=...)` | `GET /api/v1/twitter/web/fetch_user_post_tweet` | 获取用户发帖/Get user post |
| `fetch_user_profile(screen_name=..., rest_id=...)` | `GET /api/v1/twitter/web/fetch_user_profile` | 获取用户资料/Get user profile |
| `fetch_user_tweet_replies(screen_name, cursor=...)` | `GET /api/v1/twitter/web/fetch_user_tweet_replies` | 获取用户推文回复/Get user tweet replies |

## `client.wechat_channels`

**Class:** `tikhub.resources.wechat_channels.WechatChannels` (sync) / `AsyncWechatChannels` (async)

**Endpoints:** 10

| Method | Endpoint | Summary |
|---|---|---|
| `fetch_comments(id, lastBuffer=..., comment_id=...)` | `POST /api/v1/wechat_channels/fetch_comments` | 微信视频号评论/WeChat Channels Comments |
| `fetch_default_search(keywords, session_buffer=...)` | `POST /api/v1/wechat_channels/fetch_default_search` | 微信视频号默认搜索/WeChat Channels Default Search |
| `fetch_home_page(username, last_buffer=...)` | `POST /api/v1/wechat_channels/fetch_home_page` | 微信视频号主页/WeChat Channels Home Page |
| `fetch_hot_words()` | `GET /api/v1/wechat_channels/fetch_hot_words` | 微信视频号热门话题/WeChat Channels Hot Topics |
| `fetch_live_history(username)` | `GET /api/v1/wechat_channels/fetch_live_history` | 微信视频号直播回放/WeChat Channels Live History |
| `fetch_search_latest(keywords)` | `GET /api/v1/wechat_channels/fetch_search_latest` | 微信视频号搜索最新视频/WeChat Channels Search Latest Videos |
| `fetch_search_ordinary(keywords)` | `GET /api/v1/wechat_channels/fetch_search_ordinary` | 微信视频号综合搜索/WeChat Channels Comprehensive Search |
| `fetch_user_search(keywords, page=...)` | `GET /api/v1/wechat_channels/fetch_user_search` | 微信视频号用户搜索/WeChat Channels User Search |
| `fetch_user_search_v2(keywords=..., page=...)` | `GET /api/v1/wechat_channels/fetch_user_search_v2` | 微信视频号用户搜索V2/WeChat Channels User Search V2 |
| `fetch_video_detail(id=..., exportId=...)` | `GET /api/v1/wechat_channels/fetch_video_detail` | 微信视频号视频详情/WeChat Channels Video Detail |

## `client.wechat_media_platform_web`

**Class:** `tikhub.resources.wechat_media_platform_web.WechatMediaPlatformWeb` (sync) / `AsyncWechatMediaPlatformWeb` (async)

**Endpoints:** 10

| Method | Endpoint | Summary |
|---|---|---|
| `fetch_mp_article_ad(url)` | `GET /api/v1/wechat_mp/web/fetch_mp_article_ad` | 获取微信公众号广告/Get Wechat MP Article Ad |
| `fetch_mp_article_comment_list(url, comment_id=..., buffer=...)` | `GET /api/v1/wechat_mp/web/fetch_mp_article_comment_list` | 获取微信公众号文章评论列表/Get Wechat MP Article Comment List |
| `fetch_mp_article_comment_reply_list(comment_id, content_id, url=..., offset=...)` | `GET /api/v1/wechat_mp/web/fetch_mp_article_comment_reply_list` | 获取微信公众号文章评论回复列表/Get Wechat MP Article Comment Reply List |
| `fetch_mp_article_detail_html(url)` | `GET /api/v1/wechat_mp/web/fetch_mp_article_detail_html` | 获取微信公众号文章详情的HTML/Get Wechat MP Article Detail HTML |
| `fetch_mp_article_detail_json(url)` | `GET /api/v1/wechat_mp/web/fetch_mp_article_detail_json` | 获取微信公众号文章详情的JSON/Get Wechat MP Article Detail JSON |
| `fetch_mp_article_list(ghid, offset=...)` | `GET /api/v1/wechat_mp/web/fetch_mp_article_list` | 获取微信公众号文章列表/Get Wechat MP Article List |
| `fetch_mp_article_read_count(url, comment_id)` | `GET /api/v1/wechat_mp/web/fetch_mp_article_read_count` | 获取微信公众号文章阅读量/Get Wechat MP Article Read Count |
| `fetch_mp_article_url(sogou_url)` | `GET /api/v1/wechat_mp/web/fetch_mp_article_url` | 获取微信公众号文章永久链接/Get Wechat MP Article URL |
| `fetch_mp_article_url_conversion(url)` | `GET /api/v1/wechat_mp/web/fetch_mp_article_url_conversion` | 获取微信公众号长链接转短链接/Get Wechat MP Long URL to Short URL |
| `fetch_mp_related_articles(url)` | `GET /api/v1/wechat_mp/web/fetch_mp_related_articles` | 获取微信公众号关联文章/Get Wechat MP Related Articles |

## `client.weibo_app`

**Class:** `tikhub.resources.weibo_app.WeiboApp` (sync) / `AsyncWeiboApp` (async)

**Endpoints:** 20

| Method | Endpoint | Summary |
|---|---|---|
| `fetch_ai_smart_search(query, page=...)` | `GET /api/v1/weibo/app/fetch_ai_smart_search` | AI智搜/AI Smart Search |
| `fetch_home_recommend_feed(page=..., count=...)` | `GET /api/v1/weibo/app/fetch_home_recommend_feed` | 获取首页推荐Feed流/Get home recommend feed |
| `fetch_hot_search(category=..., page=..., count=..., region_name=...)` | `GET /api/v1/weibo/app/fetch_hot_search` | 获取热搜榜/Get hot search |
| `fetch_hot_search_categories()` | `GET /api/v1/weibo/app/fetch_hot_search_categories` | 获取热搜分类列表/Get hot search categories |
| `fetch_search_all(query, page=..., search_type=...)` | `GET /api/v1/weibo/app/fetch_search_all` | 综合搜索/Comprehensive search |
| `fetch_status_comments(status_id, max_id=..., sort_type=...)` | `GET /api/v1/weibo/app/fetch_status_comments` | 获取微博评论/Get post comments |
| `fetch_status_detail(status_id)` | `GET /api/v1/weibo/app/fetch_status_detail` | 获取微博详情/Get post detail |
| `fetch_status_likes(status_id, attitude_type=...)` | `GET /api/v1/weibo/app/fetch_status_likes` | 获取微博点赞列表/Get post likes |
| `fetch_status_reposts(status_id, max_id=...)` | `GET /api/v1/weibo/app/fetch_status_reposts` | 获取微博转发列表/Get post reposts |
| `fetch_user_album(uid, since_id=...)` | `GET /api/v1/weibo/app/fetch_user_album` | 获取用户相册/Get user album |
| `fetch_user_articles(uid, since_id=...)` | `GET /api/v1/weibo/app/fetch_user_articles` | 获取用户文章列表/Get user articles |
| `fetch_user_audios(uid, since_id=...)` | `GET /api/v1/weibo/app/fetch_user_audios` | 获取用户音频列表/Get user audios |
| `fetch_user_info(uid)` | `GET /api/v1/weibo/app/fetch_user_info` | 获取用户信息/Get user information |
| `fetch_user_info_detail(uid)` | `GET /api/v1/weibo/app/fetch_user_info_detail` | 获取用户详细信息/Get user detail information |
| `fetch_user_profile_feed(uid, since_id=...)` | `GET /api/v1/weibo/app/fetch_user_profile_feed` | 获取用户主页动态/Get user profile feed |
| `fetch_user_super_topics(uid, page=...)` | `GET /api/v1/weibo/app/fetch_user_super_topics` | 获取用户参与的超话列表/Get user super topics |
| `fetch_user_timeline(uid, page=..., filter_type=..., month=...)` | `GET /api/v1/weibo/app/fetch_user_timeline` | 获取用户发布的微博/Get user timeline |
| `fetch_user_videos(uid, since_id=...)` | `GET /api/v1/weibo/app/fetch_user_videos` | 获取用户视频列表/Get user videos |
| `fetch_video_detail(mid)` | `GET /api/v1/weibo/app/fetch_video_detail` | 获取视频详情/Get video detail |
| `fetch_video_featured_feed(page=...)` | `GET /api/v1/weibo/app/fetch_video_featured_feed` | 获取短视频精选Feed流/Get video featured feed |

## `client.weibo_web`

**Class:** `tikhub.resources.weibo_web.WeiboWeb` (sync) / `AsyncWeiboWeb` (async)

**Endpoints:** 11

| Method | Endpoint | Summary |
|---|---|---|
| `fetch_channel_feed(channel_name=..., page=...)` | `GET /api/v1/weibo/web/fetch_channel_feed` | 根据频道名称获取热门内容/Get channel feed by name |
| `fetch_comment_replies(cid, max_id=...)` | `GET /api/v1/weibo/web/fetch_comment_replies` | 获取评论子评论/Get comment replies |
| `fetch_config_list()` | `GET /api/v1/weibo/web/fetch_config_list` | 获取频道配置列表/Get channel config list |
| `fetch_hot_search()` | `GET /api/v1/weibo/web/fetch_hot_search` | 获取热搜榜/Get hot search ranking |
| `fetch_post_comments(post_id, mid, max_id=..., max_id_type=...)` | `GET /api/v1/weibo/web/fetch_post_comments` | 获取微博评论/Get post comments |
| `fetch_post_detail(post_id)` | `GET /api/v1/weibo/web/fetch_post_detail` | 获取微博详情/Get post detail |
| `fetch_search(keyword, page=..., search_type=..., time_scope=...)` | `GET /api/v1/weibo/web/fetch_search` | 搜索微博/Search Weibo |
| `fetch_search_topics()` | `GET /api/v1/weibo/web/fetch_search_topics` | 获取搜索页热搜词/Get search page hot topics |
| `fetch_trend_top(containerid, page=...)` | `GET /api/v1/weibo/web/fetch_trend_top` | 获取频道热门趋势/Get channel trend top |
| `fetch_user_info(uid)` | `GET /api/v1/weibo/web/fetch_user_info` | 获取用户信息/Get user information |
| `fetch_user_posts(uid, page=..., since_id=...)` | `GET /api/v1/weibo/web/fetch_user_posts` | 获取用户微博列表/Get user posts |

## `client.weibo_web_v2`

**Class:** `tikhub.resources.weibo_web_v2.WeiboWebV2` (sync) / `AsyncWeiboWebV2` (async)

**Endpoints:** 33

| Method | Endpoint | Summary |
|---|---|---|
| `check_allow_comment_with_pic(id)` | `GET /api/v1/weibo/web_v2/check_allow_comment_with_pic` | 检查微博是否允许带图评论/Check if Weibo allows image comments |
| `fetch_advanced_search(q, search_type=..., include_type=..., timescope=..., page=...)` | `GET /api/v1/weibo/web_v2/fetch_advanced_search` | 微博高级搜索/Weibo Advanced Search |
| `fetch_ai_related_search(keyword)` | `GET /api/v1/weibo/web_v2/fetch_ai_related_search` | 微博AI搜索内容扩展/Weibo AI Search Content Extension |
| `fetch_ai_search(query)` | `GET /api/v1/weibo/web_v2/fetch_ai_search` | 微博智能搜索/Weibo AI Search |
| `fetch_all_groups()` | `GET /api/v1/weibo/web_v2/fetch_all_groups` | 获取所有分组信息/Get all groups information |
| `fetch_city_list(normalized=...)` | `GET /api/v1/weibo/web_v2/fetch_city_list` | 地区省市映射/Region City List |
| `fetch_entertainment_ranking()` | `GET /api/v1/weibo/web_v2/fetch_entertainment_ranking` | 获取微博文娱榜单/Get Weibo entertainment ranking |
| `fetch_hot_ranking_timeline(ranking_type, since_id=..., max_id=..., count=...)` | `GET /api/v1/weibo/web_v2/fetch_hot_ranking_timeline` | 获取微博热门榜单时间轴/Get hot ranking timeline |
| `fetch_hot_search()` | `GET /api/v1/weibo/web_v2/fetch_hot_search` | 获取微博热搜榜单/Get Weibo hot search ranking |
| `fetch_hot_search_index()` | `GET /api/v1/weibo/web_v2/fetch_hot_search_index` | 获取微博热搜词条(10条)/Get Weibo hot search index (10 items) |
| `fetch_hot_search_summary()` | `GET /api/v1/weibo/web_v2/fetch_hot_search_summary` | 获取微博完整热搜榜单(50条)/Get Weibo complete hot search ranking (50 items) |
| `fetch_life_ranking()` | `GET /api/v1/weibo/web_v2/fetch_life_ranking` | 获取微博生活榜单/Get Weibo life ranking |
| `fetch_pic_search(query, page=...)` | `GET /api/v1/weibo/web_v2/fetch_pic_search` | 图片搜索/Weibo picture search |
| `fetch_post_comments(id, count=..., max_id=...)` | `GET /api/v1/weibo/web_v2/fetch_post_comments` | 获取微博评论/Get Weibo comments |
| `fetch_post_detail(id, is_get_long_text=...)` | `GET /api/v1/weibo/web_v2/fetch_post_detail` | 获取单个作品数据/Get single post data |
| `fetch_post_sub_comments(id, count=..., max_id=...)` | `GET /api/v1/weibo/web_v2/fetch_post_sub_comments` | 获取微博子评论/Get Weibo sub-comments |
| `fetch_realtime_search(query, page=...)` | `GET /api/v1/weibo/web_v2/fetch_realtime_search` | 实时搜索/Weibo Realtime Search |
| `fetch_similar_search(keyword)` | `GET /api/v1/weibo/web_v2/fetch_similar_search` | 获取微博相似搜索词推荐/Get Weibo similar search recommendations |
| `fetch_social_ranking()` | `GET /api/v1/weibo/web_v2/fetch_social_ranking` | 获取微博社会榜单/Get Weibo social ranking |
| `fetch_topic_search(query, page=...)` | `GET /api/v1/weibo/web_v2/fetch_topic_search` | 话题搜索/Weibo topic search |
| `fetch_user_basic_info(uid)` | `GET /api/v1/weibo/web_v2/fetch_user_basic_info` | 获取用户基本信息/Get user basic information |
| `fetch_user_fans(uid, page=...)` | `GET /api/v1/weibo/web_v2/fetch_user_fans` | 获取用户粉丝列表/Get user fans list |
| `fetch_user_following(uid, page=...)` | `GET /api/v1/weibo/web_v2/fetch_user_following` | 获取用户关注列表/Get user following list |
| `fetch_user_info(uid=..., custom=...)` | `GET /api/v1/weibo/web_v2/fetch_user_info` | 获取用户信息/Get user information |
| `fetch_user_original_posts(uid, page=..., since_id=...)` | `GET /api/v1/weibo/web_v2/fetch_user_original_posts` | 获取微博用户原创微博数据/Get Weibo user original posts |
| `fetch_user_posts(uid, page=..., feature=..., since_id=...)` | `GET /api/v1/weibo/web_v2/fetch_user_posts` | 获取微博用户文章数据/Get Weibo user posts |
| `fetch_user_recommend_timeline(refresh=..., group_id=..., containerid=..., extparam=..., max_id=..., count=...)` | `GET /api/v1/weibo/web_v2/fetch_user_recommend_timeline` | 获取微博主页推荐时间轴/Get user recommend timeline |
| `fetch_user_search(query=..., page=..., region=..., auth=..., gender=..., age=..., nickname=..., tag=..., school=..., work=...)` | `GET /api/v1/weibo/web_v2/fetch_user_search` | 用户搜索/User search |
| `fetch_user_video_collection_detail(cid, cursor=..., tab_code=...)` | `GET /api/v1/weibo/web_v2/fetch_user_video_collection_detail` | 获取用户微博视频收藏夹详情/Get user video collection detail |
| `fetch_user_video_collection_list(uid)` | `GET /api/v1/weibo/web_v2/fetch_user_video_collection_list` | 获取用户微博视频收藏夹列表/Get user video collection list |
| `fetch_user_video_list(uid, cursor=...)` | `GET /api/v1/weibo/web_v2/fetch_user_video_list` | 获取微博用户全部视频/Get user all videos |
| `fetch_video_search(query, mode=..., page=...)` | `GET /api/v1/weibo/web_v2/fetch_video_search` | 视频搜索（热门/全部）/Weibo video search (hot/all) |
| `search_user_posts(uid, q=..., page=..., starttime=..., endtime=..., hasori=..., hasret=..., hastext=..., haspic=..., hasvideo=..., hasmusic=...)` | `GET /api/v1/weibo/web_v2/search_user_posts` | 搜索用户微博/Search user posts |

## `client.xiaohongshu_app`

**Class:** `tikhub.resources.xiaohongshu_app.XiaohongshuApp` (sync) / `AsyncXiaohongshuApp` (async)

**Endpoints:** 12

| Method | Endpoint | Summary |
|---|---|---|
| `extract_share_info(share_link)` | `GET /api/v1/xiaohongshu/app/extract_share_info` | 提取分享链接信息/Extract share link info |
| `get_note_comments(note_id, start=..., sort_strategy=...)` | `GET /api/v1/xiaohongshu/app/get_note_comments` | 获取笔记评论/Get note comments |
| `get_note_info(note_id=..., share_text=...)` | `GET /api/v1/xiaohongshu/app/get_note_info` | 获取笔记信息 V1/Get note info V1 |
| `get_note_info_v2(note_id=..., share_text=...)` | `GET /api/v1/xiaohongshu/app/get_note_info_v2` | 获取笔记信息 V2 (蒲公英商家后台)/Get note info V2 (Pugongying Business Backend) |
| `get_notes_by_topic(page_id, first_load_time, sort=..., session_id=..., last_note_ct=..., last_note_id=..., cursor_score=...)` | `GET /api/v1/xiaohongshu/app/get_notes_by_topic` | [已弃用/Deprecated] 根据话题标签获取作品/Get notes by topic |
| `get_product_detail(sku_id)` | `GET /api/v1/xiaohongshu/app/get_product_detail` | 获取商品详情/Get product detail |
| `get_sub_comments(note_id, comment_id, start=...)` | `GET /api/v1/xiaohongshu/app/get_sub_comments` | 获取子评论/Get sub comments |
| `get_user_id_and_xsec_token(share_link)` | `GET /api/v1/xiaohongshu/app/get_user_id_and_xsec_token` | 从分享链接中提取用户ID和xsec_token/Extract user ID and xsec_token from share link |
| `get_user_info(user_id)` | `GET /api/v1/xiaohongshu/app/get_user_info` | 获取用户信息/Get user info |
| `get_user_notes(user_id, cursor=...)` | `GET /api/v1/xiaohongshu/app/get_user_notes` | 获取用户作品列表/Get user notes |
| `search_notes(keyword, page, search_id=..., session_id=..., sort_type=..., filter_note_type=..., filter_note_time=...)` | `GET /api/v1/xiaohongshu/app/search_notes` | 搜索笔记/Search notes |
| `search_products(keyword, page, search_id=..., session_id=..., sort=..., scope=..., service_guarantee=..., min_price=..., max_price=..., super_promotion=...)` | `GET /api/v1/xiaohongshu/app/search_products` | 搜索商品/Search products |

## `client.xiaohongshu_app_v2`

**Class:** `tikhub.resources.xiaohongshu_app_v2.XiaohongshuAppV2` (sync) / `AsyncXiaohongshuAppV2` (async)

**Endpoints:** 21

| Method | Endpoint | Summary |
|---|---|---|
| `get_creator_hot_inspiration_feed(cursor=...)` | `GET /api/v1/xiaohongshu/app_v2/get_creator_hot_inspiration_feed` | 获取创作者热点灵感列表/Get creator hot inspiration feed |
| `get_creator_inspiration_feed(cursor=..., tab=..., source=...)` | `GET /api/v1/xiaohongshu/app_v2/get_creator_inspiration_feed` | 获取创作者推荐灵感列表/Get creator inspiration feed |
| `get_image_note_detail(note_id=..., share_text=...)` | `GET /api/v1/xiaohongshu/app_v2/get_image_note_detail` | 获取图文笔记详情/Get image note detail |
| `get_mixed_note_detail(note_id=..., share_text=...)` | `GET /api/v1/xiaohongshu/app_v2/get_mixed_note_detail` | 获取首页推荐流笔记详情/Get mixed note detail from feed |
| `get_note_comments(note_id=..., share_text=..., cursor=..., index=..., pageArea=..., sort_strategy=...)` | `GET /api/v1/xiaohongshu/app_v2/get_note_comments` | 获取笔记评论列表/Get note comments |
| `get_note_sub_comments(comment_id, note_id=..., share_text=..., cursor=..., index=...)` | `GET /api/v1/xiaohongshu/app_v2/get_note_sub_comments` | 获取笔记二级评论列表/Get note sub comments |
| `get_product_detail(sku_id, source=..., pre_page=...)` | `GET /api/v1/xiaohongshu/app_v2/get_product_detail` | 获取商品详情/Get product detail |
| `get_product_recommendations(sku_id, cursor_score=..., region=...)` | `GET /api/v1/xiaohongshu/app_v2/get_product_recommendations` | 获取商品推荐列表/Get product recommendations |
| `get_product_review_overview(sku_id, tab=...)` | `GET /api/v1/xiaohongshu/app_v2/get_product_review_overview` | 获取商品评论总览/Get product review overview |
| `get_product_reviews(sku_id, page=..., sort_strategy_type=..., share_pics_only=..., from_page=...)` | `GET /api/v1/xiaohongshu/app_v2/get_product_reviews` | 获取商品评论列表/Get product reviews |
| `get_topic_feed(page_id, sort=..., cursor_score=..., last_note_id=..., last_note_ct=..., session_id=..., first_load_time=..., source=...)` | `GET /api/v1/xiaohongshu/app_v2/get_topic_feed` | 获取话题笔记列表/Get topic feed |
| `get_topic_info(page_id, source=..., note_id=...)` | `GET /api/v1/xiaohongshu/app_v2/get_topic_info` | 获取话题详情/Get topic info |
| `get_user_faved_notes(user_id=..., share_text=..., cursor=...)` | `GET /api/v1/xiaohongshu/app_v2/get_user_faved_notes` | 获取用户收藏笔记列表/Get user faved notes |
| `get_user_info(user_id=..., share_text=...)` | `GET /api/v1/xiaohongshu/app_v2/get_user_info` | 获取用户信息/Get user info |
| `get_user_posted_notes(user_id=..., share_text=..., cursor=...)` | `GET /api/v1/xiaohongshu/app_v2/get_user_posted_notes` | 获取用户笔记列表/Get user posted notes |
| `get_video_note_detail(note_id=..., share_text=...)` | `GET /api/v1/xiaohongshu/app_v2/get_video_note_detail` | 获取视频笔记详情/Get video note detail |
| `search_groups(keyword, page_no=..., search_id=..., source=..., is_recommend=...)` | `GET /api/v1/xiaohongshu/app_v2/search_groups` | 搜索群聊/Search groups |
| `search_images(keyword, page=..., search_id=..., search_session_id=..., word_request_id=..., source=...)` | `GET /api/v1/xiaohongshu/app_v2/search_images` | 搜索图片/Search images |
| `search_notes(keyword, page=..., sort_type=..., note_type=..., time_filter=..., search_id=..., search_session_id=..., source=..., ai_mode=...)` | `GET /api/v1/xiaohongshu/app_v2/search_notes` | 搜索笔记/Search notes |
| `search_products(keyword, page=..., search_id=..., source=...)` | `GET /api/v1/xiaohongshu/app_v2/search_products` | 搜索商品/Search products |
| `search_users(keyword, page=..., search_id=..., source=...)` | `GET /api/v1/xiaohongshu/app_v2/search_users` | 搜索用户/Search users |

## `client.xiaohongshu_web`

**Class:** `tikhub.resources.xiaohongshu_web.XiaohongshuWeb` (sync) / `AsyncXiaohongshuWeb` (async)

**Endpoints:** 17

| Method | Endpoint | Summary |
|---|---|---|
| `get_home_recommend(feed_type=..., need_filter_image=..., cursor_score=..., cookie=..., proxy=...)` | `POST /api/v1/xiaohongshu/web/get_home_recommend` | 获取首页推荐/Get home recommend |
| `get_note_comment_replies(note_id, comment_id, lastCursor=...)` | `GET /api/v1/xiaohongshu/web/get_note_comment_replies` | 获取笔记评论回复 V1/Get note comment replies V1 |
| `get_note_comments(note_id, lastCursor=...)` | `GET /api/v1/xiaohongshu/web/get_note_comments` | 获取笔记评论 V1/Get note comments V1 |
| `get_note_id_and_xsec_token(share_text)` | `GET /api/v1/xiaohongshu/web/get_note_id_and_xsec_token` | 通过分享链接获取小红书的Note ID 和 xsec_token/Get Xiaohongshu Note ID and xsec_token by share link |
| `get_note_info_v2(note_id=..., share_text=...)` | `GET /api/v1/xiaohongshu/web/get_note_info_v2` | 获取笔记信息 V2/Get note info V2 |
| `get_note_info_v4(note_id=..., share_text=...)` | `GET /api/v1/xiaohongshu/web/get_note_info_v4` | 获取笔记信息 V4/Get note info V4 |
| `get_note_info_v5(note_id=..., xsec_token=..., cookie=..., proxy=...)` | `POST /api/v1/xiaohongshu/web/get_note_info_v5` | 获取笔记信息 V5 (自带Cookie)/Get note info V5 (Self-provided Cookie) |
| `get_note_info_v7(note_id=..., share_text=...)` | `GET /api/v1/xiaohongshu/web/get_note_info_v7` | 获取笔记信息 V7/Get note info V7 |
| `get_product_info(share_text=..., item_id=..., xsec_token=...)` | `GET /api/v1/xiaohongshu/web/get_product_info` | 获取小红书商品信息/Get Xiaohongshu product info |
| `get_user_info(user_id)` | `GET /api/v1/xiaohongshu/web/get_user_info` | 获取用户信息 V1/Get user info V1 |
| `get_user_info_v2(user_id=..., share_text=...)` | `GET /api/v1/xiaohongshu/web/get_user_info_v2` | 获取用户信息 V2/Get user info V2 |
| `get_user_notes_v2(user_id, lastCursor=...)` | `GET /api/v1/xiaohongshu/web/get_user_notes_v2` | 获取用户的笔记 V2/Get user notes V2 |
| `get_visitor_cookie(proxy=...)` | `GET /api/v1/xiaohongshu/web/get_visitor_cookie` | 获取游客Cookie/Get visitor cookie |
| `search_notes(keyword, page=..., sort=..., noteType=..., noteTime=...)` | `GET /api/v1/xiaohongshu/web/search_notes` | 搜索笔记/Search notes |
| `search_notes_v3(keyword, page=..., sort=..., noteType=..., noteTime=...)` | `GET /api/v1/xiaohongshu/web/search_notes_v3` | 搜索笔记 V3/Search notes V3 |
| `search_users(keyword, page=...)` | `GET /api/v1/xiaohongshu/web/search_users` | 搜索用户/Search users |
| `sign(path=..., data=..., cookie=...)` | `POST /api/v1/xiaohongshu/web/sign` | 小红书Web签名/Xiaohongshu Web sign |

## `client.xiaohongshu_web_v2`

**Class:** `tikhub.resources.xiaohongshu_web_v2.XiaohongshuWebV2` (sync) / `AsyncXiaohongshuWebV2` (async)

**Endpoints:** 18

| Method | Endpoint | Summary |
|---|---|---|
| `fetch_feed_notes(note_id)` | `GET /api/v1/xiaohongshu/web_v2/fetch_feed_notes` | 获取单一笔记和推荐笔记 V1 (已弃用)/Fetch one note and feed notes V1 (deprecated) |
| `fetch_feed_notes_v2(note_id)` | `GET /api/v1/xiaohongshu/web_v2/fetch_feed_notes_v2` | 获取单一笔记和推荐笔记 V2/Fetch one note and feed notes V2(v2稳定, 推荐使用此接口) |
| `fetch_feed_notes_v3(short_url)` | `GET /api/v1/xiaohongshu/web_v2/fetch_feed_notes_v3` | 获取单一笔记和推荐笔记 V3/Fetch one note and feed notes V3(通过短链获取笔记详情) |
| `fetch_feed_notes_v4(note_id)` | `GET /api/v1/xiaohongshu/web_v2/fetch_feed_notes_v4` | 获取单一笔记和推荐笔记 V4 (互动量有延迟)/Fetch one note and feed notes V4 (interaction volume has a delay) |
| `fetch_feed_notes_v5(note_id)` | `GET /api/v1/xiaohongshu/web_v2/fetch_feed_notes_v5` | 获取单一笔记和推荐笔记 V5 (互动量有缺失)/Fetch one note and feed notes V5 (interaction volume has a missing) |
| `fetch_follower_list(user_id, cursor=...)` | `GET /api/v1/xiaohongshu/web_v2/fetch_follower_list` | 获取用户粉丝列表/Fetch follower list |
| `fetch_following_list(user_id, cursor=...)` | `GET /api/v1/xiaohongshu/web_v2/fetch_following_list` | 获取用户关注列表/Fetch following list |
| `fetch_home_notes(user_id, cursor=...)` | `GET /api/v1/xiaohongshu/web_v2/fetch_home_notes` | 获取Web用户主页笔记/Fetch web user profile notes |
| `fetch_home_notes_app(user_id, cursor=...)` | `GET /api/v1/xiaohongshu/web_v2/fetch_home_notes_app` | 获取App用户主页笔记/Fetch App user home notes |
| `fetch_hot_list()` | `GET /api/v1/xiaohongshu/web_v2/fetch_hot_list` | 获取小红书热榜/Fetch Xiaohongshu hot list |
| `fetch_note_comments(note_id, cursor=...)` | `GET /api/v1/xiaohongshu/web_v2/fetch_note_comments` | 获取笔记评论/Fetch note comments |
| `fetch_note_image(note_id)` | `GET /api/v1/xiaohongshu/web_v2/fetch_note_image` | 获取小红书笔记图片/Fetch Xiaohongshu note image |
| `fetch_product_list(user_id, page=...)` | `GET /api/v1/xiaohongshu/web_v2/fetch_product_list` | 获取小红书商品列表/Fetch Xiaohongshu product list |
| `fetch_search_notes(keywords, page=..., sort_type=..., note_type=...)` | `GET /api/v1/xiaohongshu/web_v2/fetch_search_notes` | 获取搜索笔记/Fetch search notes |
| `fetch_search_users(keywords, page=...)` | `GET /api/v1/xiaohongshu/web_v2/fetch_search_users` | 获取搜索用户/Fetch search users |
| `fetch_sub_comments(note_id, comment_id, cursor=...)` | `GET /api/v1/xiaohongshu/web_v2/fetch_sub_comments` | 获取子评论/Fetch sub comments |
| `fetch_user_info(user_id)` | `GET /api/v1/xiaohongshu/web_v2/fetch_user_info` | 获取用户信息/Fetch user info |
| `fetch_user_info_app(user_id)` | `GET /api/v1/xiaohongshu/web_v2/fetch_user_info_app` | 获取App用户信息/Fetch App user info |

## `client.xiaohongshu_web_v3`

**Class:** `tikhub.resources.xiaohongshu_web_v3.XiaohongshuWebV3` (sync) / `AsyncXiaohongshuWebV3` (async)

**Endpoints:** 11

| Method | Endpoint | Summary |
|---|---|---|
| `fetch_homefeed(num=..., cursor_score=..., category=..., need_filter_image=...)` | `GET /api/v1/xiaohongshu/web_v3/fetch_homefeed` | 获取首页推荐/Fetch homepage feed |
| `fetch_homefeed_categories()` | `GET /api/v1/xiaohongshu/web_v3/fetch_homefeed_categories` | 获取首页分类列表/Fetch homepage categories |
| `fetch_note_comments(note_id, cursor=...)` | `GET /api/v1/xiaohongshu/web_v3/fetch_note_comments` | 获取笔记评论/Fetch note comments |
| `fetch_note_detail(note_id, xsec_token=...)` | `GET /api/v1/xiaohongshu/web_v3/fetch_note_detail` | 获取笔记详情/Fetch note detail |
| `fetch_search_notes(keyword, page=..., sort=..., note_type=...)` | `GET /api/v1/xiaohongshu/web_v3/fetch_search_notes` | 搜索笔记/Search notes |
| `fetch_search_suggest(keyword=...)` | `GET /api/v1/xiaohongshu/web_v3/fetch_search_suggest` | 获取搜索联想词/Fetch search suggestions |
| `fetch_search_users(keyword, page=...)` | `GET /api/v1/xiaohongshu/web_v3/fetch_search_users` | 搜索用户/Search users |
| `fetch_sub_comments(note_id, root_comment_id, num=..., cursor=...)` | `GET /api/v1/xiaohongshu/web_v3/fetch_sub_comments` | 获取子评论/Fetch sub comments |
| `fetch_trending()` | `GET /api/v1/xiaohongshu/web_v3/fetch_trending` | 获取热搜词/Fetch trending keywords |
| `fetch_user_info(user_id)` | `GET /api/v1/xiaohongshu/web_v3/fetch_user_info` | 获取用户信息/Fetch user info |
| `fetch_user_notes(user_id, cursor=..., num=...)` | `GET /api/v1/xiaohongshu/web_v3/fetch_user_notes` | 获取用户笔记列表/Fetch user notes |

## `client.xigua_app_v2`

**Class:** `tikhub.resources.xigua_app_v2.XiguaAppV2` (sync) / `AsyncXiguaAppV2` (async)

**Endpoints:** 7

| Method | Endpoint | Summary |
|---|---|---|
| `fetch_one_video(item_id)` | `GET /api/v1/xigua/app/v2/fetch_one_video` | 获取单个作品数据/Get single video data |
| `fetch_one_video_play_url(item_id)` | `GET /api/v1/xigua/app/v2/fetch_one_video_play_url` | 获取单个作品的播放链接/Get single video play URL |
| `fetch_one_video_v2(item_id)` | `GET /api/v1/xigua/app/v2/fetch_one_video_v2` | 获取单个作品数据 V2/Get single video data V2 |
| `fetch_user_info(user_id)` | `GET /api/v1/xigua/app/v2/fetch_user_info` | 个人信息/Personal information |
| `fetch_user_post_list(user_id, max_behot_time=...)` | `GET /api/v1/xigua/app/v2/fetch_user_post_list` | 获取个人作品列表/Get user post list |
| `fetch_video_comment_list(item_id, offset=..., count=...)` | `GET /api/v1/xigua/app/v2/fetch_video_comment_list` | 视频评论列表/Video comment list |
| `search_video(keyword, offset=..., order_type=..., min_duration=..., max_duration=...)` | `GET /api/v1/xigua/app/v2/search_video` | 搜索视频/Search video |

## `client.youtube_web`

**Class:** `tikhub.resources.youtube_web.YoutubeWeb` (sync) / `AsyncYoutubeWeb` (async)

**Endpoints:** 21

| Method | Endpoint | Summary |
|---|---|---|
| `get_channel_description(channel_id=..., continuation_token=..., language_code=..., country_code=..., need_format=...)` | `GET /api/v1/youtube/web/get_channel_description` | 获取频道描述信息/Get channel description |
| `get_channel_id(channel_name)` | `GET /api/v1/youtube/web/get_channel_id` | 获取频道ID/Get channel ID |
| `get_channel_id_v2(channel_url)` | `GET /api/v1/youtube/web/get_channel_id_v2` | 从频道URL获取频道ID V2/Get channel ID from URL V2 |
| `get_channel_info(channel_id)` | `GET /api/v1/youtube/web/get_channel_info` | 获取频道信息/Get channel information |
| `get_channel_short_videos(channel_id, continuation_token=...)` | `GET /api/v1/youtube/web/get_channel_short_videos` | 获取频道短视频/Get channel short videos |
| `get_channel_url(channel_id)` | `GET /api/v1/youtube/web/get_channel_url` | 从频道ID获取频道URL/Get channel URL from channel ID |
| `get_channel_videos(channel_id, continuation_token=...)` | `GET /api/v1/youtube/web/get_channel_videos` | 获取频道视频 V1（即将过时，优先使用 V2）/Get channel videos V1 (deprecated soon, use V2 first) |
| `get_channel_videos_v2(channel_id, lang=..., sortBy=..., contentType=..., nextToken=...)` | `GET /api/v1/youtube/web/get_channel_videos_v2` | 获取频道视频 V2/Get channel videos V2 |
| `get_channel_videos_v3(channel_id, language_code=..., country_code=..., continuation_token=..., need_format=...)` | `GET /api/v1/youtube/web/get_channel_videos_v3` | 获取频道视频 V3/Get channel videos V3 |
| `get_general_search(search_query, language_code=..., country_code=..., time_zone=..., upload_time=..., duration=..., content_type=..., feature=..., sort_by=..., continuation_token=...)` | `GET /api/v1/youtube/web/get_general_search` | 综合搜索（支持过滤条件）/General search with filters |
| `get_relate_video(video_id, continuation_token=...)` | `GET /api/v1/youtube/web/get_relate_video` | 获取推荐视频/Get related videos |
| `get_shorts_search(search_query, language_code=..., country_code=..., time_zone=..., upload_time=..., sort_by=..., continuation_token=..., filter_mixed_content=...)` | `GET /api/v1/youtube/web/get_shorts_search` | YouTube Shorts短视频搜索/YouTube Shorts search |
| `get_trending_videos(language_code=..., country_code=..., section=...)` | `GET /api/v1/youtube/web/get_trending_videos` | 获取趋势视频/Get trending videos |
| `get_video_comment_replies(continuation_token, language_code=..., country_code=..., need_format=...)` | `GET /api/v1/youtube/web/get_video_comment_replies` | 获取视频二级评论/Get video sub comments |
| `get_video_comments(video_id, language_code=..., country_code=..., sort_by=..., continuation_token=..., need_format=...)` | `GET /api/v1/youtube/web/get_video_comments` | 获取视频评论/Get video comments |
| `get_video_info(video_id, url_access=..., lang=..., videos=..., audios=..., subtitles=..., related=...)` | `GET /api/v1/youtube/web/get_video_info` | 获取视频信息 V1/Get video information V1 |
| `get_video_info_v2(video_id)` | `GET /api/v1/youtube/web/get_video_info_v2` | 获取视频信息 V2/Get video information V2 |
| `get_video_info_v3(video_id, language_code=...)` | `GET /api/v1/youtube/web/get_video_info_v3` | 获取视频详情 V3/Get video information V3 |
| `get_video_subtitles(subtitle_url, format=..., fix_overlap=..., target_lang=...)` | `GET /api/v1/youtube/web/get_video_subtitles` | 获取视频字幕/Get video subtitles |
| `search_channel(channel_id, search_query, language_code=..., country_code=..., continuation_token=...)` | `GET /api/v1/youtube/web/search_channel` | 搜索频道/Search channel |
| `search_video(search_query, language_code=..., order_by=..., country_code=..., continuation_token=...)` | `GET /api/v1/youtube/web/search_video` | 搜索视频/Search video |

## `client.youtube_web_v2`

**Class:** `tikhub.resources.youtube_web_v2.YoutubeWebV2` (sync) / `AsyncYoutubeWebV2` (async)

**Endpoints:** 19

| Method | Endpoint | Summary |
|---|---|---|
| `get_channel_description(channel_id=..., continuation_token=..., language_code=..., country_code=..., need_format=...)` | `GET /api/v1/youtube/web_v2/get_channel_description` | 获取频道描述信息/Get channel description |
| `get_channel_id(channel_url)` | `GET /api/v1/youtube/web_v2/get_channel_id` | 从频道URL获取频道ID /Get channel ID from URL |
| `get_channel_shorts(channel_id=..., channel_url=..., continuation_token=..., need_format=...)` | `GET /api/v1/youtube/web_v2/get_channel_shorts` | 获取频道短视频列表/Get channel shorts |
| `get_channel_url(channel_id)` | `GET /api/v1/youtube/web_v2/get_channel_url` | 从频道ID获取频道URL/Get channel URL from channel ID |
| `get_channel_videos(channel_id, language_code=..., country_code=..., continuation_token=..., need_format=...)` | `GET /api/v1/youtube/web_v2/get_channel_videos` | 获取频道视频 /Get channel videos |
| `get_general_search(search_query, language_code=..., country_code=..., time_zone=..., upload_time=..., duration=..., content_type=..., feature=..., sort_by=..., continuation_token=...)` | `GET /api/v1/youtube/web_v2/get_general_search` | 综合搜索（原始数据，推荐使用V2）/General search (raw data, recommend V2) |
| `get_general_search_v2(keyword=..., continuation_token=..., upload_date=..., type=..., duration=..., features=..., sort_by=...)` | `GET /api/v1/youtube/web_v2/get_general_search_v2` | 综合搜索V2/General search V2 |
| `get_related_videos(video_id=..., video_url=..., need_format=...)` | `GET /api/v1/youtube/web_v2/get_related_videos` | 获取视频相似内容/Get related videos |
| `get_search_suggestions(keyword, language=..., region=...)` | `GET /api/v1/youtube/web_v2/get_search_suggestions` | 获取搜索推荐词/Get search suggestions |
| `get_shorts_search(search_query, language_code=..., country_code=..., time_zone=..., upload_time=..., sort_by=..., continuation_token=..., filter_mixed_content=...)` | `GET /api/v1/youtube/web_v2/get_shorts_search` | Shorts搜索（原始数据，推荐使用V2）/Shorts search (raw data, recommend V2) |
| `get_shorts_search_v2(keyword=..., continuation_token=..., upload_date=..., sort_by=...)` | `GET /api/v1/youtube/web_v2/get_shorts_search_v2` | Shorts搜索V2/Shorts search V2 |
| `get_signed_stream_url(itag, video_id=..., video_url=...)` | `GET /api/v1/youtube/web_v2/get_signed_stream_url` | 获取已签名的视频流URL/Get signed video stream URL |
| `get_video_captions(video_id=..., video_url=..., language_code=..., format=...)` | `GET /api/v1/youtube/web_v2/get_video_captions` | 获取视频字幕/Get video captions |
| `get_video_comment_replies(continuation_token, language_code=..., country_code=..., need_format=...)` | `GET /api/v1/youtube/web_v2/get_video_comment_replies` | 获取视频二级评论/Get video sub comments |
| `get_video_comments(video_id, language_code=..., country_code=..., sort_by=..., continuation_token=..., need_format=...)` | `GET /api/v1/youtube/web_v2/get_video_comments` | 获取视频评论/Get video comments |
| `get_video_info(video_id, language_code=..., need_format=...)` | `GET /api/v1/youtube/web_v2/get_video_info` | 获取视频详情 /Get video information |
| `get_video_streams(video_id=..., video_url=...)` | `GET /api/v1/youtube/web_v2/get_video_streams` | 获取视频流信息/Get video streams info |
| `get_video_streams_v2(video_id=..., video_url=...)` | `GET /api/v1/youtube/web_v2/get_video_streams_v2` | 获取视频流信息 V2/Get video streams info V2 |
| `search_channels(keyword=..., continuation_token=..., need_format=...)` | `GET /api/v1/youtube/web_v2/search_channels` | 搜索频道/Search channels |

## `client.zhihu_web`

**Class:** `tikhub.resources.zhihu_web.ZhihuWeb` (sync) / `AsyncZhihuWeb` (async)

**Endpoints:** 34

| Method | Endpoint | Summary |
|---|---|---|
| `fetch_ai_search(message_content)` | `GET /api/v1/zhihu/web/fetch_ai_search` | 获取知乎AI搜索/Get Zhihu AI Search |
| `fetch_ai_search_result(message_id)` | `GET /api/v1/zhihu/web/fetch_ai_search_result` | 获取知乎AI搜索结果/Get Zhihu AI Search Result |
| `fetch_article_search_v3(keyword, offset=..., limit=..., show_all_topics=..., search_source=..., search_hash_id=..., vertical=..., sort=..., time_interval=..., vertical_info=...)` | `GET /api/v1/zhihu/web/fetch_article_search_v3` | 获取知乎文章搜索V3/Get Zhihu Article Search V3 |
| `fetch_column_article_detail(article_id)` | `GET /api/v1/zhihu/web/fetch_column_article_detail` | 获取知乎专栏文章详情/Get Zhihu Column Article Detail |
| `fetch_column_articles(column_id, limit=..., offset=...)` | `GET /api/v1/zhihu/web/fetch_column_articles` | 获取知乎专栏文章列表/Get Zhihu Column Articles |
| `fetch_column_comment_config(article_id)` | `GET /api/v1/zhihu/web/fetch_column_comment_config` | 获取知乎专栏评论区配置/Get Zhihu Column Comment Config |
| `fetch_column_recommend(article_id, limit=..., offset=...)` | `GET /api/v1/zhihu/web/fetch_column_recommend` | 获取知乎相似专栏推荐/Get Zhihu Similar Column Recommend |
| `fetch_column_relationship(article_id)` | `GET /api/v1/zhihu/web/fetch_column_relationship` | 获取知乎专栏文章互动关系/Get Zhihu Column Article Relationship |
| `fetch_column_search_v3(keyword, offset=..., limit=..., search_hash_id=...)` | `GET /api/v1/zhihu/web/fetch_column_search_v3` | 获取知乎专栏搜索V3/Get Zhihu Column Search V3 |
| `fetch_comment_v5(answer_id, order_by=..., limit=..., offset=...)` | `GET /api/v1/zhihu/web/fetch_comment_v5` | 获取知乎评论区V5/Get Zhihu Comment V5 |
| `fetch_ebook_search_v3(keyword, offset=..., limit=..., search_hash_id=...)` | `GET /api/v1/zhihu/web/fetch_ebook_search_v3` | 获取知乎电子书搜索V3/Get Zhihu Ebook Search V3 |
| `fetch_hot_list(limit=..., desktop=...)` | `GET /api/v1/zhihu/web/fetch_hot_list` | 获取知乎首页热榜/Get Zhihu Hot List |
| `fetch_hot_recommend(offset=..., page_number=..., session_token=...)` | `GET /api/v1/zhihu/web/fetch_hot_recommend` | 获取知乎首页推荐/Get Zhihu Hot Recommend |
| `fetch_preset_search()` | `GET /api/v1/zhihu/web/fetch_preset_search` | 获取知乎搜索预设词/Get Zhihu Preset Search |
| `fetch_question_answers(question_id, cursor=..., limit=..., offset=..., order=..., session_id=...)` | `GET /api/v1/zhihu/web/fetch_question_answers` | 获取知乎问题回答列表/Get Zhihu Question Answers |
| `fetch_recommend_followees()` | `GET /api/v1/zhihu/web/fetch_recommend_followees` | 获取知乎推荐关注列表/Get Zhihu Recommend Followees |
| `fetch_salt_search_v3(keyword, offset=..., limit=..., search_hash_id=...)` | `GET /api/v1/zhihu/web/fetch_salt_search_v3` | 获取知乎盐选内容搜索V3/Get Zhihu Salt Search V3 |
| `fetch_scholar_search_v3(keyword, offset=..., limit=..., body=...)` | `POST /api/v1/zhihu/web/fetch_scholar_search_v3` | 获取知乎论文搜索V3/Get Zhihu Scholar Search V3 |
| `fetch_search_recommend()` | `GET /api/v1/zhihu/web/fetch_search_recommend` | 获取知乎搜索发现/Get Zhihu Search Recommend |
| `fetch_search_suggest(keyword)` | `GET /api/v1/zhihu/web/fetch_search_suggest` | 知乎搜索预测词/Get Zhihu Search Suggest |
| `fetch_sub_comment_v5(comment_id, order_by=..., limit=..., offset=...)` | `GET /api/v1/zhihu/web/fetch_sub_comment_v5` | 获取知乎子评论区V5/Get Zhihu Sub Comment V5 |
| `fetch_topic_search_v3(keyword, offset=..., limit=...)` | `GET /api/v1/zhihu/web/fetch_topic_search_v3` | 获取知乎话题搜索V3/Get Zhihu Topic Search V3 |
| `fetch_user_articles(user_url_token, offset=..., limit=..., sort_type=...)` | `GET /api/v1/zhihu/web/fetch_user_articles` | 获取知乎用户的文章列表/Get Zhihu User Articles |
| `fetch_user_follow_collections(user_url_token, offset=..., limit=...)` | `GET /api/v1/zhihu/web/fetch_user_follow_collections` | 获取知乎用户关注的收藏/Get Zhihu User Follow Collections |
| `fetch_user_follow_columns(user_url_token, offset=..., limit=...)` | `GET /api/v1/zhihu/web/fetch_user_follow_columns` | 获取知乎用户订阅的专栏/Get Zhihu User Columns |
| `fetch_user_follow_questions(user_url_token, offset=..., limit=...)` | `GET /api/v1/zhihu/web/fetch_user_follow_questions` | 获取知乎用户关注的问题/Get Zhihu User Follow Questions |
| `fetch_user_follow_topics(user_url_token, offset=..., limit=...)` | `GET /api/v1/zhihu/web/fetch_user_follow_topics` | 获取知乎用户关注的话题/Get Zhihu User Follow Topics |
| `fetch_user_followees(user_url_token, offset=..., limit=...)` | `GET /api/v1/zhihu/web/fetch_user_followees` | 获取知乎用户关注列表/Get Zhihu User Following |
| `fetch_user_followers(user_url_token, offset=..., limit=...)` | `GET /api/v1/zhihu/web/fetch_user_followers` | 获取知乎用户粉丝列表/Get Zhihu User Followers |
| `fetch_user_included_articles(user_url_token, offset=..., limit=...)` | `GET /api/v1/zhihu/web/fetch_user_included_articles` | 获取知乎用户的被收录文章列表/Get Zhihu User Included Articles |
| `fetch_user_info(user_url_token)` | `GET /api/v1/zhihu/web/fetch_user_info` | 获取知乎用户信息/Get Zhihu User Info |
| `fetch_user_search_v3(keyword, offset=..., limit=...)` | `GET /api/v1/zhihu/web/fetch_user_search_v3` | 获取知乎用户搜索V3/Get Zhihu User Search V3 |
| `fetch_video_list(offset=..., limit=...)` | `GET /api/v1/zhihu/web/fetch_video_list` | 获取知乎首页视频榜/Get Zhihu Video List |
| `fetch_video_search_v3(keyword, limit=..., offset=..., search_hash_id=...)` | `GET /api/v1/zhihu/web/fetch_video_search_v3` | 获取知乎视频搜索V3/Get Zhihu Video Search V3 |
