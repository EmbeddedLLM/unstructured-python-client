"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from enum import Enum
from typing import List, Optional
from unstructured_client import utils


class ChunkingStrategy(str, Enum, metaclass=utils.OpenEnumMeta):
    BASIC = 'basic'
    BY_PAGE = 'by_page'
    BY_SIMILARITY = 'by_similarity'
    BY_TITLE = 'by_title'


@dataclasses.dataclass
class Files:
    content: bytes = dataclasses.field(metadata={'multipart_form': { 'content': True }})
    file_name: str = dataclasses.field(metadata={'multipart_form': { 'field_name': 'files' }})
    



class OutputFormat(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""The format of the response. Supported formats are application/json and text/csv. Default: application/json."""
    APPLICATION_JSON = 'application/json'
    TEXT_CSV = 'text/csv'


class Strategy(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""The strategy to use for partitioning PDF/image. Options are fast, hi_res, auto. Default: auto"""
    FAST = 'fast'
    HI_RES = 'hi_res'
    AUTO = 'auto'
    OCR_ONLY = 'ocr_only'


@dataclasses.dataclass
class PartitionParameters:
    UNSET='__SPEAKEASY_UNSET__'
    files: Files = dataclasses.field(metadata={'multipart_form': { 'file': True }})
    r"""The file to extract"""
    chunking_strategy: Optional[ChunkingStrategy] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'chunking_strategy' }})
    r"""Use one of the supported strategies to chunk the returned elements. Currently supports: 'basic', 'by_page', 'by_similarity', or 'by_title'"""
    combine_under_n_chars: Optional[int] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'combine_under_n_chars' }})
    r"""If chunking strategy is set, combine elements until a section reaches a length of n chars. Default: 500"""
    coordinates: Optional[bool] = dataclasses.field(default=False, metadata={'multipart_form': { 'field_name': 'coordinates' }})
    r"""If true, return coordinates for each element. Default: false"""
    encoding: Optional[str] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'encoding' }})
    r"""The encoding method used to decode the text input. Default: utf-8"""
    extract_image_block_types: Optional[List[str]] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'extract_image_block_types' }})
    r"""The types of elements to extract, for use in extracting image blocks as base64 encoded data stored in metadata fields"""
    gz_uncompressed_content_type: Optional[str] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'gz_uncompressed_content_type' }})
    r"""If file is gzipped, use this content type after unzipping"""
    hi_res_model_name: Optional[str] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'hi_res_model_name' }})
    r"""The name of the inference model used when strategy is hi_res"""
    include_orig_elements: Optional[bool] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'include_orig_elements' }})
    r"""When a chunking strategy is specified, each returned chunk will include the elements consolidated to form that chunk as `.metadata.orig_elements`. Default: true."""
    include_page_breaks: Optional[bool] = dataclasses.field(default=False, metadata={'multipart_form': { 'field_name': 'include_page_breaks' }})
    r"""If True, the output will include page breaks if the filetype supports it. Default: false"""
    languages: Optional[List[str]] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'languages' }})
    r"""The languages present in the document, for use in partitioning and/or OCR"""
    max_characters: Optional[int] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'max_characters' }})
    r"""If chunking strategy is set, cut off new sections after reaching a length of n chars (hard max). Default: 500"""
    multipage_sections: Optional[bool] = dataclasses.field(default=True, metadata={'multipart_form': { 'field_name': 'multipage_sections' }})
    r"""If chunking strategy is set, determines if sections can span multiple sections. Default: true"""
    new_after_n_chars: Optional[int] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'new_after_n_chars' }})
    r"""If chunking strategy is set, cut off new sections after reaching a length of n chars (soft max). Default: 1500"""
    ocr_languages: Optional[List[str]] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'ocr_languages' }})
    r"""The languages present in the document, for use in partitioning and/or OCR"""
    output_format: Optional[OutputFormat] = dataclasses.field(default=OutputFormat.APPLICATION_JSON, metadata={'multipart_form': { 'field_name': 'output_format' }})
    r"""The format of the response. Supported formats are application/json and text/csv. Default: application/json."""
    overlap: Optional[int] = dataclasses.field(default=0, metadata={'multipart_form': { 'field_name': 'overlap' }})
    r"""Specifies the length of a string ('tail') to be drawn from each chunk and prefixed to the next chunk as a context-preserving mechanism. By default, this only applies to split-chunks where an oversized element is divided into multiple chunks by text-splitting. Default: 0"""
    overlap_all: Optional[bool] = dataclasses.field(default=False, metadata={'multipart_form': { 'field_name': 'overlap_all' }})
    r"""When `True`, apply overlap between 'normal' chunks formed from whole elements and not subject to text-splitting. Use this with caution as it entails a certain level of 'pollution' of otherwise clean semantic chunk boundaries. Default: False"""
    pdf_infer_table_structure: Optional[bool] = dataclasses.field(default=True, metadata={'multipart_form': { 'field_name': 'pdf_infer_table_structure' }})
    r"""Deprecated! Use skip_infer_table_types to opt out of table extraction for any file type. If False and strategy=hi_res, no Table Elements will be extracted from pdf files regardless of skip_infer_table_types contents."""
    similarity_threshold: Optional[float] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'similarity_threshold' }})
    r"""A value between 0.0 and 1.0 describing the minimum similarity two elements must have to be included in the same chunk. Note that similar elements may be separated to meet chunk-size criteria; this value can only guarantees that two elements with similarity below the threshold will appear in separate chunks."""
    skip_infer_table_types: Optional[List[str]] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'skip_infer_table_types' }})
    r"""The document types that you want to skip table extraction with. Default: []"""
    split_pdf_concurrency_level: Optional[int] = dataclasses.field(default=5, metadata={'multipart_form': { 'field_name': 'split_pdf_concurrency_level' }})
    r"""When `split_pdf_page` is set to `True`, this parameter specifies the number of workers used for sending requests when the PDF is split on the client side. It's an internal parameter for the Python client and is not sent to the backend."""
    split_pdf_page: Optional[bool] = dataclasses.field(default=False, metadata={'multipart_form': { 'field_name': 'split_pdf_page' }})
    r"""This parameter determines if the PDF file should be split on the client side. It's an internal parameter for the Python client and is not sent to the backend."""
    starting_page_number: Optional[int] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'starting_page_number' }})
    r"""When PDF is split into pages before sending it into the API, providing this information will allow the page number to be assigned correctly. Introduced in 1.0.27."""
    strategy: Optional[Strategy] = dataclasses.field(default=Strategy.AUTO, metadata={'multipart_form': { 'field_name': 'strategy' }})
    r"""The strategy to use for partitioning PDF/image. Options are fast, hi_res, auto. Default: auto"""
    unique_element_ids: Optional[bool] = dataclasses.field(default=False, metadata={'multipart_form': { 'field_name': 'unique_element_ids' }})
    r"""When `True`, assign UUIDs to element IDs, which guarantees their uniqueness (useful when using them as primary keys in database). Otherwise a SHA-256 of element text is used. Default: False"""
    xml_keep_tags: Optional[bool] = dataclasses.field(default=False, metadata={'multipart_form': { 'field_name': 'xml_keep_tags' }})
    r"""If True, will retain the XML tags in the output. Otherwise it will simply extract the text from within the tags. Only applies to partition_xml."""
    

