export default function TimeAgo({timestamp}) {

  const timeAgo = (timestamp) => {
    const seconds = Math.floor((new Date() - new Date(timestamp)) / 1000);
    let interval = seconds / 31536000;

    if (interval > 1) {
      return Math.floor(interval) + "years";
    }
    interval = seconds / 2592000;
    if (interval > 1) {
      return Math.floor(interval) + "months";
    }
    interval = seconds / 86400;
    if (interval > 1) {
      return Math.floor(interval) + "days";
    }
    interval = seconds / 3600;
    if (interval > 1) {
      return Math.floor(interval) + "hours";
    }
    interval = seconds / 60;
    if (interval > 1) {
      return Math.floor(interval) + "min";
    }
    return Math.floor(seconds) + "sec";
  }

  return (
    <span>{timeAgo(timestamp)}</span>
  );
}