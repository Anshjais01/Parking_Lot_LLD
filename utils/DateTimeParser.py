'''
package org.nailyourinterview.lld.parking_lot.utils;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Locale;

public class DateTimeParser {
    public static LocalDateTime parse(String input) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("d MMM h:mm a yyyy", Locale.ENGLISH);
        return LocalDateTime.parse(input, formatter);
    }
}'''

import re
from datetime import datetime


class DateTimeParser:
    """Parser utility to convert date-time strings into datetime objects."""

    PATTERN = "%d %b %I:%M %p %Y"

    _MONTHS = {
        "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
        "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12
    }

    _REGEX_PATTERN = re.compile(
        r"^(\d{1,2})\s+([A-Za-z]{3,9})\s+(\d{1,2}):(\d{2})\s+([AaPp][Mm])\s+(\d{4})$"
    )

    @classmethod
    def parse(cls, input_val) -> datetime:
        """
        Parse date time string formatted like 'd MMM h:mm a yyyy' in English locale
        (e.g. '27 Oct 10:30 PM 2026' or '5 Jun 8:05 AM 2024').
        Also accepts datetime objects directly or ISO format strings.
        """
        if isinstance(input_val, datetime):
            return input_val

        if not input_val or not isinstance(input_val, str):
            raise ValueError(f"Invalid input: expected non-empty date string, got {input_val!r}")

        clean_str = input_val.strip()

        # Primary parser: Regex-based to ensure English locale support regardless of system locale
        match = cls._REGEX_PATTERN.match(clean_str)
        if match:
            day = int(match.group(1))
            month_key = match.group(2)[:3].lower()
            if month_key in cls._MONTHS:
                month = cls._MONTHS[month_key]
                hour = int(match.group(3))
                minute = int(match.group(4))
                ampm = match.group(5).upper()
                year = int(match.group(6))

                if ampm == "PM" and hour != 12:
                    hour += 12
                elif ampm == "AM" and hour == 12:
                    hour = 0

                return datetime(year, month, day, hour, minute)

        # Fallback 1: standard strptime
        try:
            return datetime.strptime(clean_str, cls.PATTERN)
        except ValueError:
            pass

        # Fallback 2: ISO format
        try:
            return datetime.fromisoformat(clean_str)
        except Exception:
            pass

        # Fallback 3: other common formats
        for fmt in (
            "%d %b %I:%M %p %Y",
            "%d %B %I:%M %p %Y",
            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%d %H:%M",
        ):
            try:
                return datetime.strptime(clean_str, fmt)
            except ValueError:
                continue

        raise ValueError(
            f"Unable to parse datetime string '{input_val}'. "
            f"Expected pattern 'd MMM h:mm a yyyy' (e.g. '27 Oct 10:30 PM 2026')."
        )
