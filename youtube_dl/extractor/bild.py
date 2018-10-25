# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor
from ..utils import (
    base_url,
    int_or_none,
    unescapeHTML,
    urljoin,
)


class BildIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?bild\.de/(?:[^/]+/)+(?P<display_id>[^/]+)-(?P<id>\d+)(?:,auto=true)?\.bild\.html'
    IE_DESC = 'Bild.de'
    _TEST = {
        'url': 'http://www.bild.de/video/clip/apple-ipad-air/das-koennen-die-neuen-ipads-38184146.bild.html',
        'md5': 'dd495cbd99f2413502a1713a1156ac8a',
        'info_dict': {
            'id': '38184146',
            'ext': 'mp4',
            'title': 'Das können die  neuen iPads',
            'description': 'md5:a4058c4fa2a804ab59c00d7244bbf62f',
            'thumbnail': r're:^https?://.*\.jpg$',
            'duration': 196,
        }
    }

    def _real_extract(self, url):
        video_id = self._match_id(url)

        # if we didn't get a direct link to the video, try to find it on the page
        if 'bild.de/video/clip/' not in url:
            json_url = self._search_regex(
                r'data-video-json="(.*?)"',
                self._download_webpage(url, video_id), video_id)
            video_data = self._download_json(
                urljoin(base_url(url), json_url), video_id)
        else:
            video_data = self._download_json(
                url.split('.bild.html')[0] + ',view=json.bild.html', video_id)

        return {
            'id': video_id,
            'title': unescapeHTML(video_data['title']).strip(),
            'description': unescapeHTML(video_data.get('description')),
            'url': video_data['clipList'][0]['srces'][0]['src'],
            'thumbnail': video_data.get('poster'),
            'duration': int_or_none(video_data.get('durationSec')),
        }
