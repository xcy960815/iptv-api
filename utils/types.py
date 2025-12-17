from typing import TypedDict, Literal, Union, Optional, Dict

try:  # Python 3.11+ has NotRequired in typing
    from typing import NotRequired  # type: ignore
except ImportError:
    from typing_extensions import NotRequired  # type: ignore

OriginType = Literal["hls", "local", "whitelist", "subscribe", "hotel", "multicast", "online_search"]
IPvType = Optional[str]


class ChannelData(TypedDict):
    """
    Channel data types, including url, date, resolution, origin and ipv_type
    """
    id: int
    url: str
    host: str
    date: NotRequired[Optional[str]]
    resolution: NotRequired[Optional[str]]
    origin: OriginType
    ipv_type: IPvType
    location: NotRequired[Optional[str]]
    isp: NotRequired[Optional[str]]
    headers: NotRequired[Optional[Dict[str, str]]]
    catchup: NotRequired[Optional[Dict[str, str]]]
    extra_info: NotRequired[str]


CategoryChannelData = dict[str, dict[str, list[ChannelData]]]


class TestResult(TypedDict):
    """
    Test result types, including speed, delay, resolution
    """
    speed: Optional[Union[int, float]]
    delay: Optional[Union[int, float]]
    resolution: Optional[Union[int, str]]


TestResultCacheData = dict[str, list[TestResult]]

ChannelTestResult = Union[ChannelData, TestResult]
